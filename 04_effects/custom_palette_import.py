"""Custom Palette Import Example

Demonstrates how to create custom effects from color palettes,
using the unified 90-palette system.
"""

from styledconsole import Console, EffectSpec, EFFECTS, PALETTES, get_palette

console = Console()

print()
console.text("🎨 CUSTOM PALETTE IMPORT", color="cyan", bold=True)
print("=" * 80)
print()

# Method 1: Create effect from color list
console.text("Method 1: Create from hex color list", color="yellow", bold=True)
print("-" * 80)

# Create custom gradient from any color list
cyberpunk_colors = ["#711c91", "#ea00d9", "#0abdc6", "#133e7c", "#091833"]
cyberpunk_effect = EffectSpec.multi_stop(cyberpunk_colors)

console.frame(
    ["Purple tech", "Hot magenta", "Neon cyan", "Deep blue", "Dark night"],
    effect=cyberpunk_effect,
    title="Custom Cyberpunk Gradient",
    border="heavy",
)
print()

# Method 2: Load palette from unified palette system
console.text("Method 2: Load from 90 curated palettes", color="yellow", bold=True)
print("-" * 80)

beach_effect = EffectSpec.from_palette("beach")
console.frame(
    ["Mint green", "Sandy yellow", "Coral", "Mustard", "Turquoise"],
    effect=beach_effect,
    title="Beach Palette (5 colors)",
    border="rounded",
)
print()

# Method 3: Load palette with custom direction
console.text("Method 3: Horizontal gradient from palette", color="yellow", bold=True)
print("-" * 80)

sunset_horizontal = EFFECTS.load_palette("aesthetic", direction="horizontal")

console.frame(
    ["Aesthetic colors flow left to right"],
    effect=sunset_horizontal,
    title="Horizontal Aesthetic Palette",
    border="rounded",
)
print()

# Method 4: Border-only effect from palette
console.text("Method 4: Border-only palette effect", color="yellow", bold=True)
print("-" * 80)

vaporwave_border = EffectSpec.from_palette("vaporwave", target="border")

console.frame(
    ["Plain content", "with colorful", "gradient borders"],
    effect=vaporwave_border,
    title="Vaporwave Border",
    border="double",
)
print()

# Show all available palettes
console.text("Available palettes (first 20):", color="green", bold=True)
print("-" * 80)
all_palettes = sorted(PALETTES.keys())
for name in all_palettes[:20]:
    palette = get_palette(name)
    console.text(f"  • {name} ({len(palette['colors'])} colors)", color="white")
print(f"  ... and {len(all_palettes) - 20} more! Total: {len(all_palettes)} palettes")
print()

console.text("✅ Custom palette import examples complete!", color="lime", bold=True)
console.text(
    "   Use EffectSpec.from_palette() or EFFECTS.load_palette() for any of 90 palettes!",
    color="white",
)
print()
