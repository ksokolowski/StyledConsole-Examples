#!/usr/bin/env python3
"""
Effect Showcase - Modern effect= API
=====================================

Demonstrates the comprehensive effect= API introduced in v0.9.9.3, showing:
1. Named effect presets from EFFECTS registry
2. Custom gradients with EffectSpec.gradient()
3. Multi-stop gradients with EffectSpec.multi_stop()
4. Rainbow effects with EffectSpec.rainbow()
5. Effect targets (content, border, both)

The effect= parameter is the modern way to apply visual effects to frames and banners.
"""

from styledconsole import Console, EFFECTS, EffectSpec, icons

console = Console()


def main():
    console.clear()
    console.newline()
    
    console.banner("EFFECTS", effect="fire")
    console.text("Modern effect= API Showcase", color="cyan", bold=True)
    console.newline()

    # ==================================================================
    # 1. NAMED EFFECT PRESETS
    # ==================================================================
    
    console.text("🎨 1. Named Effect Presets", color="yellow", bold=True)
    console.text("   Use effect='preset_name' or EFFECTS.preset_name", color="dim")
    console.newline()

    # Fire effect
    console.frame(
        f"{icons.FIRE} Fire effect for hot/urgent content",
        effect="fire",
        title="effect='fire'",
        border="rounded",
        width=60,
    )

    # Ocean effect
    console.frame(
        f"{icons.WATER_WAVE} Ocean effect for calm/cool content",
        effect="ocean",
        title="effect='ocean'",
        border="rounded",
        width=60,
    )

    # Matrix effect
    console.frame(
        f"{icons.LAPTOP} Matrix effect for tech/code content",
        effect="matrix",
        title="EFFECTS.matrix",
        border="heavy",
        width=60,
    )

    console.newline()

    # ==================================================================
    # 2. CUSTOM GRADIENTS
    # ==================================================================
    
    console.text("🌈 2. Custom Gradients with EffectSpec.gradient()", color="yellow", bold=True)
    console.text("   Create gradients with any start/end colors", color="dim")
    console.newline()

    # Simple 2-color gradient
    console.frame(
        [
            "Custom gradient from red to blue",
            "Direction: vertical (default)",
            "Target: content (default)",
        ],
        effect=EffectSpec.gradient("red", "blue"),
        title="EffectSpec.gradient('red', 'blue')",
        border="rounded",
        width=60,
    )

    # Horizontal gradient
    console.frame(
        "Horizontal gradient from yellow to purple",
        effect=EffectSpec.gradient("yellow", "purple", direction="horizontal"),
        title="direction='horizontal'",
        border="double",
        width=60,
    )

    # Border-only gradient
    console.frame(
        [
            "Plain content",
            "Gradient applied to borders only",
            "Good for subtle visual hierarchy",
        ],
        effect=EffectSpec.gradient("cyan", "magenta", target="border"),
        title="target='border'",
        border="heavy",
        width=60,
    )

    console.newline()

    # ==================================================================
    # 3. MULTI-STOP GRADIENTS
    # ==================================================================
    
    console.text("🎨 3. Multi-Stop Gradients", color="yellow", bold=True)
    console.text("   Use 3+ colors for complex gradients", color="dim")
    console.newline()

    # 3-color gradient
    console.frame(
        [
            "Three-color gradient",
            "Colors: red → yellow → green",
            "Perfect for status indicators",
        ],
        effect=EffectSpec.multi_stop(["red", "yellow", "green"]),
        title="EffectSpec.multi_stop(['red', 'yellow', 'green'])",
        border="rounded",
        width=60,
    )

    # Vaporwave preset (multi-stop example)
    console.frame(
        [
            "Vaporwave aesthetic",
            "Pink → Purple → Cyan gradient",
            "80s retro vibes",
        ],
        effect="vaporwave",
        title="effect='vaporwave'",
        border="thick",
        width=60,
    )

    console.newline()

    # ==================================================================
    # 4. RAINBOW EFFECTS
    # ==================================================================
    
    console.text("🌈 4. Rainbow Effects", color="yellow", bold=True)
    console.text("   Full spectrum rainbow gradients", color="dim")
    console.newline()

    # Standard rainbow
    console.frame(
        [
            "Standard rainbow gradient",
            "Full 7-color spectrum",
            "Red → Orange → Yellow → Green → Blue → Indigo → Violet",
        ],
        effect="rainbow",
        title="effect='rainbow'",
        border="rounded",
        width=65,
    )

    # Rainbow neon (brighter colors)
    console.frame(
        [
            "Rainbow Neon",
            "Vibrant, saturated colors",
            "Perfect for eye-catching displays",
        ],
        effect="rainbow_neon",
        title="effect='rainbow_neon'",
        border="heavy",
        width=65,
    )

    # Rainbow pastel (softer colors)
    console.frame(
        [
            "Rainbow Pastel",
            "Soft, muted colors",
            "Gentle on the eyes",
        ],
        effect="rainbow_pastel",
        title="EFFECTS.rainbow_pastel",
        border="double",
        width=65,
    )

    console.newline()

    # ==================================================================
    # 5. BORDER-ONLY PRESETS
    # ==================================================================
    
    console.text("📦 5. Border-Only Presets", color="yellow", bold=True)
    console.text("   Preset effects applied to borders only", color="dim")
    console.newline()

    console.frame(
        [
            "Content stays plain",
            "Only borders are colored",
            "Subtle visual enhancement",
        ],
        effect="border_fire",
        title="effect='border_fire'",
        border="heavy",
        width=60,
    )

    console.frame(
        [
            "Border ocean gradient",
            "Cool blue borders",
            "Clean content area",
        ],
        effect="border_ocean",
        title="effect='border_ocean'",
        border="rounded",
        width=60,
    )

    console.newline()

    # ==================================================================
    # 6. BANNER EFFECTS
    # ==================================================================
    
    console.text("🎪 6. Banner Effects", color="yellow", bold=True)
    console.text("   Effects work on ASCII art banners too!", color="dim")
    console.newline()

    console.banner("FIRE", effect="fire")
    console.banner("RAINBOW", effect="rainbow_neon")
    console.banner("OCEAN", effect="ocean")

    console.newline()

    # ==================================================================
    # SUMMARY
    # ==================================================================
    
    console.frame(
        [
            f"{icons.SPARKLES} Effect System Summary:",
            "",
            "• 32 built-in presets in EFFECTS registry",
            "• Custom gradients with any colors",
            "• Multi-stop gradients (3+ colors)",
            "• Rainbow effects (standard, neon, pastel)",
            "• Target: content, border, or both",
            "• Direction: vertical, horizontal, diagonal",
            "",
            "See EFFECTS registry for all presets:",
            "  from styledconsole import EFFECTS",
            "  print(list(EFFECTS))",
        ],
        title=f"{icons.INFORMATION} Modern effect= API",
        effect=EffectSpec.gradient("#00ffff", "#ff00ff", target="border"),
        border="double",
        width=70,
    )

    console.newline(2)


if __name__ == "__main__":
    main()
