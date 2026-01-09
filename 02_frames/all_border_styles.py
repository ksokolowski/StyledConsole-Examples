#!/usr/bin/env python3
"""All Border Styles - Visual catalog of frame borders.

StyledConsole provides 9 built-in border styles, each with
its own character and use case.

Usage:
    python 02_frames/all_border_styles.py
"""

from styledconsole import Console, EffectSpec, icons

console = Console()

console.banner("BORDERS", font="small", effect=EffectSpec.gradient("cyan", "blue"))
console.newline()

# =============================================================================
# The 9 Built-in Border Styles
# =============================================================================

BORDER_STYLES = [
    ("solid", "Classic single-line border. Default choice."),
    ("rounded", "Soft rounded corners. Modern, friendly feel."),
    ("double", "Double-line border. Formal, important content."),
    ("heavy", "Thick bold lines. High emphasis, warnings."),
    ("thick", "Alternative thick style. Strong presence."),
    ("rounded_thick", "Rounded with thick lines. Premium feel."),
    ("ascii", "ASCII-only characters. Maximum compatibility."),
    ("dots", "Light dotted lines. Subtle, decorative borders."),
    ("minimal", "Minimal decoration. Top/bottom only."),
]

for style, description in BORDER_STYLES:
    console.frame(
        f"{icons.BOOKMARK} {description}",
        title=f"border=\"{style}\"",
        border=style,
        border_color="cyan",
    )
    console.newline()

# =============================================================================
# Border Style Comparison Grid
# =============================================================================

console.rule("Side-by-Side Comparison")
console.newline()

# All styles to compare (excluding minimal which is special)
styles = ["solid", "rounded", "double", "heavy", "thick", "rounded_thick", "ascii", "dots"]

# Use frame_group with grid layout - auto-calculates columns based on terminal width
console.frame_group(
    [{"content": f"Style: {style}", "border": style, "border_color": "lime"} for style in styles],
    layout="grid",
    columns="auto",
    min_columns=2,
    item_width=35,
    gap=2,
)

# =============================================================================
# When to Use Each Style
# =============================================================================

console.rule("Style Guide")
console.newline()

console.frame(
    f"""
{icons.CHECK_MARK_BUTTON} solid        - Default, general purpose
{icons.CHECK_MARK_BUTTON} rounded      - Modern UI, friendly messages
{icons.CHECK_MARK_BUTTON} double       - Important notices, headers
{icons.WARNING} heavy        - Warnings, critical alerts
{icons.WARNING} thick        - High-priority content
{icons.SPARKLES} rounded_thick - Premium, polished look
{icons.GEAR} ascii        - Legacy terminals, CI logs
{icons.BOOKMARK} dots         - Light decorative borders
{icons.BOOKMARK} minimal      - Top/bottom lines only
    """.strip(),
    title="Recommended Usage",
    border="rounded",
    border_color="dodgerblue",
)
