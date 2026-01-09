"""Modern Rainbow Effects Example

Demonstrates the new effect= API for rainbow gradients:
- effect="rainbow": Smooth rainbow gradient
- effect="rainbow_neon": Vibrant neon rainbow
- effect="rainbow_pastel": Soft pastel rainbow
- EffectSpec.gradient(): Custom gradient effects
"""

from styledconsole import Console, EFFECTS, EffectSpec

console = Console()

print()
console.text("🌈 MODERN RAINBOW EFFECTS", color="cyan", bold=True)
print("=" * 80)
print()

# Test content - multiple lines to show gradient
content = [
    "Line 1 - Red spectrum",
    "Line 2 - Orange spectrum",
    "Line 3 - Yellow spectrum",
    "Line 4 - Green spectrum",
    "Line 5 - Blue spectrum",
    "Line 6 - Indigo spectrum",
    "Line 7 - Violet spectrum",
    "Line 8 - Back to red",
]

# 1. Standard rainbow effect
console.text("1️⃣  effect='rainbow' (smooth gradient):", color="yellow")
print("-" * 80)
console.frame(
    content,
    effect="rainbow",
    border="rounded",
    title="Smooth Rainbow Gradient",
)
print()

# 2. Rainbow neon preset
console.text("2️⃣  effect='rainbow_neon' (vibrant neon):", color="yellow")
print("-" * 80)
console.frame(
    content,
    effect="rainbow_neon",
    border="heavy",
    title="Neon Rainbow",
)
print()

# 3. Using EFFECTS registry
console.text("3️⃣  EFFECTS.rainbow_pastel (soft colors):", color="yellow")
print("-" * 80)
console.frame(
    ["Line 1", "Line 2", "Line 3", "Line 4"],
    effect=EFFECTS.rainbow_pastel,
    border="double",
    title="Pastel Rainbow",
)
print()

# 4. Custom gradient with EffectSpec
console.text("4️⃣  EffectSpec.gradient() (custom colors):", color="yellow")
print("-" * 80)
console.frame(
    ["Custom", "Gradient", "Effect"],
    effect=EffectSpec.gradient("gold", "purple", direction="vertical"),
    border="thick",
    title="Custom Gradient",
)
print()

# 5. Border-only gradient
console.text("5️⃣  Border-only gradient:", color="yellow")
print("-" * 80)
console.frame(
    ["Plain content", "Gradient borders only"],
    effect=EffectSpec.gradient("cyan", "magenta", target="border"),
    border="heavy",
    title="Border Gradient",
)
print()

console.text("✅ Modern effect= API showcase complete!", color="lime", bold=True)
print()
