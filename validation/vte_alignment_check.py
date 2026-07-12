#!/usr/bin/env python3
"""
VTE Alignment Validator

Programmatic stand-in for eyeballing examples in a VTE-based terminal
(Ptyxis, GNOME Terminal). VTE advances the cursor per codepoint
(GNOME/vte#2909), so this script:

1. scans every example source in the repo for emoji sequences,
2. renders each one inside a frame with the library forced into its
   VTE width mode (as if running under Ptyxis),
3. recomputes every rendered line's width with an independent emulation
   of VTE's cursor-advance algorithm,
4. fails loudly on any frame whose borders would misalign in VTE.

Run directly or via the examples runner (validation category).
"""

import os
import re
import sys
import unicodedata
from pathlib import Path

# Simulate a Ptyxis session BEFORE importing styledconsole: VTE marker
# plus a plain xterm TERM, with any host-terminal identity cleared so
# modern-terminal detection cannot win (e.g. running this from Ghostty).
os.environ["VTE_VERSION"] = "7802"
os.environ["TERM"] = "xterm-256color"
for _var in (
    "TERM_PROGRAM",
    "KITTY_WINDOW_ID",
    "WEZTERM_PANE",
    "WEZTERM_EXECUTABLE",
    "ITERM_SESSION_ID",
    "WT_SESSION",
    "STYLEDCONSOLE_MODERN_TERMINAL",
    "STYLEDCONSOLE_LEGACY_EMOJI",
):
    os.environ.pop(_var, None)

from styledconsole import Console  # noqa: E402
from styledconsole.policy import RenderPolicy  # noqa: E402
from styledconsole.utils.text import strip_ansi, visual_width  # noqa: E402

EXAMPLES_ROOT = Path(__file__).parent.parent

# Anything at/above U+2190 can render wide or zero in a terminal;
# capture runs so ZWJ/VS16/flag sequences stay intact.
EMOJI_RUN = re.compile(r"[←-\U0010FFFF][‍️\U0001F3FB-\U0001F3FF←-\U0010FFFF]*")

FRAME_WIDTH = 44


def vte_render_width(text: str) -> int:
    """Independent emulation of VTE's per-codepoint cursor advance."""
    width = 0
    for char in text:
        cp = ord(char)
        if cp != 0x00AD and (unicodedata.category(char) in ("Mn", "Me", "Cf") or cp == 0x200B):
            continue
        width += 2 if unicodedata.east_asian_width(char) in ("W", "F") else 1
    return width


def collect_emoji_from_sources() -> dict[str, list[str]]:
    """Map each emoji sequence found in example sources to its files."""
    found: dict[str, list[str]] = {}
    for path in sorted(EXAMPLES_ROOT.rglob("*.py")):
        if ".venv" in path.parts or path.name == Path(__file__).name:
            continue
        try:
            source = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for match in EMOJI_RUN.finditer(source):
            seq = match.group()
            # Skip pure box-drawing/dingbat-arrow runs that never mix
            # into content strings as emoji (borders are validated as
            # part of the rendered frame anyway)
            if all(0x2500 <= ord(c) <= 0x257F for c in seq):
                continue
            found.setdefault(seq, []).append(str(path.relative_to(EXAMPLES_ROOT)))
    return found


def main() -> int:
    from styledconsole.utils.text import _current_width_mode

    mode = _current_width_mode()
    print("=" * 70)
    print("VTE ALIGNMENT VALIDATOR (simulated Ptyxis/GNOME Terminal)")
    print("=" * 70)
    print(f"Library width mode: {mode}")
    if mode != "vte":
        print("❌ Expected 'vte' mode — detection is broken")
        return 1

    emoji_map = collect_emoji_from_sources()
    print(f"Emoji sequences found across example sources: {len(emoji_map)}")
    print()

    console = Console(policy=RenderPolicy(color=False), width=80)
    width_mismatches: list[tuple[str, int, int, str]] = []
    frame_failures: list[tuple[str, set, str]] = []

    for seq, files in sorted(emoji_map.items()):
        ours = visual_width(seq)
        vtes = vte_render_width(seq)
        if ours != vtes:
            width_mismatches.append((seq, ours, vtes, files[0]))
            continue

        rendered = console.render_frame(f"x {seq} y", title="chk", width=FRAME_WIDTH)
        line_widths = {
            vte_render_width(strip_ansi(line))
            for line in rendered.splitlines()
            if line.strip()
        }
        if line_widths != {FRAME_WIDTH}:
            frame_failures.append((seq, line_widths, files[0]))

    ok = len(emoji_map) - len(width_mismatches) - len(frame_failures)
    print(f"✅ aligned in VTE: {ok}/{len(emoji_map)}")

    if width_mismatches:
        print(f"\n❌ WIDTH MODEL MISMATCHES ({len(width_mismatches)}):")
        for seq, ours, vtes, src in width_mismatches:
            codepoints = " ".join(f"U+{ord(c):04X}" for c in seq)
            print(f"   {seq!r} ({codepoints}) ours={ours} vte={vtes}  e.g. {src}")

    if frame_failures:
        print(f"\n❌ FRAME MISALIGNMENTS ({len(frame_failures)}):")
        for seq, widths, src in frame_failures:
            print(f"   {seq!r} line widths {sorted(widths)} (want {{{FRAME_WIDTH}}})  e.g. {src}")

    if width_mismatches or frame_failures:
        return 1

    print("\n🎉 Every emoji used by the examples renders aligned under VTE")
    return 0


if __name__ == "__main__":
    sys.exit(main())
