#!/usr/bin/env python3
"""Background Layer Effects Demo.

Demonstrates the new background layer feature (v0.10.2+) that applies
gradient effects to background colors instead of foreground text.

Features shown:
- Foreground vs background gradient comparison
- Background gradients with different color schemes
- Combined foreground + background effects
- Background layer with various presets
"""

from styledconsole import Console, EffectSpec, RenderPolicy

# Use color-enabled policy to ensure colors display
console = Console(policy=RenderPolicy(color=True, unicode=True, emoji=True))

console.frame(
    "Background Layer Effects Demo",
    title="v0.10.2 Feature",
    effect="rainbow",
)
console.newline()

# =============================================================================
# 1. Foreground vs Background Comparison
# =============================================================================

console.rule("[cyan]1. Foreground vs Background Comparison[/]")
console.newline()

# Same gradient, different layers
fg_effect = EffectSpec.gradient("red", "blue", layer="foreground")
bg_effect = EffectSpec.gradient("red", "blue", layer="background")

console.text("[bold]Foreground gradient (default):[/]")
console.frame(
    "Red to Blue gradient on TEXT color",
    effect=fg_effect,
    border="rounded",
)
console.newline()

console.text("[bold]Background gradient:[/]")
console.frame(
    "Red to Blue gradient on BACKGROUND",
    effect=bg_effect,
    border="rounded",
)
console.newline()

# =============================================================================
# 2. Background Effects with Different Palettes
# =============================================================================

console.rule("[cyan]2. Background with Color Palettes[/]")
console.newline()

palettes = [
    ("ocean_depths", "Ocean Depths"),
    ("city_sunset", "City Sunset"),
    ("forest_green", "Forest Green"),
]

for palette_name, display_name in palettes:
    effect = EffectSpec.from_palette(palette_name, layer="background")
    console.frame(
        f"{display_name} palette",
        title=palette_name,
        effect=effect,
        border="rounded",
    )

console.newline()

# =============================================================================
# 3. Rainbow Background
# =============================================================================

console.rule("[cyan]3. Rainbow Background[/]")
console.newline()

rainbow_bg = EffectSpec.rainbow(layer="background")
console.frame(
    [
        "Rainbow gradient applied to background",
        "Creates a colorful backdrop effect",
        "Text remains default color for readability",
    ],
    title="Rainbow Background",
    effect=rainbow_bg,
    border="double",
)
console.newline()

# =============================================================================
# 4. Neon Background
# =============================================================================

console.rule("[cyan]4. Neon/Cyberpunk Background[/]")
console.newline()

neon_bg = EffectSpec.rainbow(neon=True, layer="background")
console.frame(
    [
        "Neon rainbow on background",
        "Vibrant cyberpunk aesthetics",
        "High saturation colors",
    ],
    title="Neon Background",
    effect=neon_bg,
    border="heavy",
)
console.newline()

# =============================================================================
# 5. Horizontal Background Gradient
# =============================================================================

console.rule("[cyan]5. Directional Background Gradients[/]")
console.newline()

horizontal_bg = EffectSpec.gradient(
    "purple", "cyan", direction="horizontal", layer="background"
)
console.frame(
    "Horizontal gradient flows left to right",
    title="Horizontal",
    effect=horizontal_bg,
    width=50,
)
console.newline()

diagonal_bg = EffectSpec.gradient(
    "yellow", "red", direction="diagonal", layer="background"
)
console.frame(
    "Diagonal gradient flows corner to corner",
    title="Diagonal",
    effect=diagonal_bg,
    width=50,
)
console.newline()

# =============================================================================
# 6. Multi-stop Background
# =============================================================================

console.rule("[cyan]6. Multi-stop Background Gradient[/]")
console.newline()

multi_bg = EffectSpec.multi_stop(
    ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#0000ff", "#8b00ff"],
    layer="background",
)
console.frame(
    [
        "Multi-stop gradient with 6 colors",
        "Creates smooth color transitions",
        "ROYGBIV spectrum on background",
    ],
    title="Spectrum",
    effect=multi_bg,
    border="rounded",
)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    [
        "Background Layer Summary:",
        "",
        "  layer='foreground'  - Colors the text (default)",
        "  layer='background'  - Colors the background",
        "",
        "Works with:",
        "  - EffectSpec.gradient()",
        "  - EffectSpec.rainbow()",
        "  - EffectSpec.multi_stop()",
        "  - EffectSpec.from_palette()",
    ],
    title="Usage",
    effect="ocean",
    border="double",
)
