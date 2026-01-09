"""Community Inspired Palettes Showcase

Demonstrates the curated effect presets inspired by popular palettes
from the community, organized by theme.
"""

from styledconsole import Console, EFFECTS

console = Console()

print()
console.text("🎨 COMMUNITY INSPIRED PALETTES", color="cyan", bold=True)
console.text("Popular color combinations from the community", color="white")
print("=" * 80)
print()

# Nature & Seasons
console.text("🌿 NATURE & SEASONS", color="green", bold=True)
print("-" * 80)

console.frame(
    ["Turquoise waters", "Golden sand", "Clear sky", "Deep ocean"],
    effect="beach",
    title="Beach",
    border="rounded",
)
print()

console.frame(
    ["Falling leaves", "Harvest orange", "Golden sunset", "Purple dusk"],
    effect="autumn",
    title="Autumn",
    border="rounded",
)
print()

console.frame(
    ["Pink blossoms", "Warm sunshine", "Fresh mint", "Clear sky"],
    effect="spring_blossom",
    title="Spring Blossom",
    border="rounded",
)
print()

console.frame(
    ["Frost", "Ice blue", "Purple twilight", "Silver mist"],
    effect="winter_frost",
    title="Winter Frost",
    border="rounded",
)
print()

# Food & Drink
console.text("☕ FOOD & DRINK", color="yellow", bold=True)
print("-" * 80)

console.frame(
    ["Dark espresso", "Rose cream", "Coral foam", "Peach foam"],
    effect="cappuccino",
    title="Cappuccino",
    border="rounded",
)
print()

console.frame(
    ["Strawberry", "Mango passion", "Lemon zest", "Kiwi green"],
    effect="tropical_juice",
    title="Tropical Juice",
    border="rounded",
)
print()

console.frame(
    ["Blueberry", "Raspberry", "Strawberry", "Grape"],
    effect="berry_smoothie",
    title="Berry Smoothie",
    border="rounded",
)
print()

# Tech & Cyber
console.text("💻 TECH & CYBER", color="magenta", bold=True)
print("-" * 80)

console.frame(
    ["Terminal prompt", "Matrix code", "Green on black", "Hacker aesthetic"],
    effect="terminal_green",
    title="Terminal Green",
    border="heavy",
)
print()

console.frame(
    ["Deep blue", "Electric", "Cyan glow", "Bright neon"],
    effect="electric_blue",
    title="Electric Blue",
    border="heavy",
)
print()

console.frame(
    ["Hot magenta", "Pink coral", "Purple tech", "Deep violet"],
    effect="cyber_magenta",
    title="Cyber Magenta",
    border="heavy",
)
print()

# Pastels
console.text("🍬 PASTELS", color="pink", bold=True)
print("-" * 80)

console.frame(
    ["Lemon", "Peach", "Bubblegum", "Lavender"],
    effect="pastel_candy",
    title="Pastel Candy",
    border="double",
)
print()

console.frame(
    ["Soft red", "Soft orange", "Soft yellow", "Soft green", "Soft blue"],
    effect="soft_rainbow",
    title="Soft Rainbow",
    border="double",
)
print()

# Dark Themes
console.text("🌙 DARK THEMES", color="white", bold=True)
print("-" * 80)

console.frame(
    ["Deep purple", "Dark violet", "Midnight purple"],
    effect="dark_purple",
    title="Dark Purple",
    border="thick",
)
print()

console.frame(
    ["Navy blue", "Almost black", "Deep indigo", "Rich purple"],
    effect="midnight",
    title="Midnight",
    border="thick",
)
print()

console.frame(
    ["Dark slate", "Charcoal grey", "Steel blue"],
    effect="carbon",
    title="Carbon",
    border="thick",
)
print()

console.text("✅ Community palette showcase complete!", color="lime", bold=True)
console.text(f"   Total available effects: {len(EFFECTS.list_all())}", color="white")
print()
