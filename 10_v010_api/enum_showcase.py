#!/usr/bin/env python3
"""v0.10.2 Enum Types Showcase.

Demonstrates the StrEnum types introduced in v0.10.2 for IDE autocomplete
and type safety. All enums are backward compatible with string values.

Enums available:
- Border: Frame border styles (ROUNDED, DOUBLE, HEAVY, etc.)
- Align: Text alignment (LEFT, CENTER, RIGHT)
- Direction: Gradient direction (VERTICAL, HORIZONTAL, DIAGONAL)
- Target: Effect target (CONTENT, BORDER, BOTH)
- Effect: 47 named effect presets
- LayoutMode: Layout modes (VERTICAL, HORIZONTAL, GRID)
- ExportFormat: Export formats (HTML, PNG, WEBP, etc.)

Benefits:
- IDE autocomplete shows all available options
- Type checking catches typos at development time
- Self-documenting code
"""

from styledconsole import Console, EffectSpec, RenderPolicy
from styledconsole.enums import Align, Border, Direction, Effect, LayoutMode, Target

# Use color-enabled policy
console = Console(policy=RenderPolicy(color=True, unicode=True, emoji=True))

console.frame(
    "v0.10.2 Enum Types Showcase",
    title="StyledConsole Enums",
    effect=Effect.RAINBOW,
)
console.newline()

# =============================================================================
# 1. Border Enum - Frame border styles
# =============================================================================

console.rule("[cyan]1. Border Enum - Frame Styles[/]")
console.newline()

# Show different border styles using enum
borders = [
    (Border.ROUNDED, "Modern, friendly"),
    (Border.DOUBLE, "Classic, formal"),
    (Border.HEAVY, "Bold, attention-grabbing"),
    (Border.MINIMAL, "Subtle, clean"),
]

for border, description in borders:
    console.frame(
        f"{description}",
        title=f"Border.{border.name}",
        border=border,  # Using enum!
        width=40,
    )

console.newline()

# =============================================================================
# 2. Effect Enum - Named presets
# =============================================================================

console.rule("[cyan]2. Effect Enum - Named Presets[/]")
console.newline()

# Semantic effects for status messages
console.text("[bold]Semantic Effects:[/]")
semantic_effects = [
    (Effect.SUCCESS, "Operation completed"),
    (Effect.WARNING, "Proceed with caution"),
    (Effect.ERROR, "Action failed"),
    (Effect.INFO, "Here's some info"),
]

for effect, message in semantic_effects:
    console.frame(
        message,
        title=f"Effect.{effect.name}",
        effect=effect,  # Using enum!
        border=Border.ROUNDED,
        width=35,
    )

console.newline()

# Themed effects
console.text("[bold]Themed Effects:[/]")
themed_effects = [
    (Effect.CYBERPUNK, "Neon future"),
    (Effect.MATRIX, "Digital rain"),
    (Effect.VAPORWAVE, "Aesthetic vibes"),
]

for effect, message in themed_effects:
    console.frame(
        message,
        title=f"Effect.{effect.name}",
        effect=effect,
        border=Border.HEAVY,
        width=35,
    )

console.newline()

# =============================================================================
# 3. Direction Enum - Gradient directions
# =============================================================================

console.rule("[cyan]3. Direction Enum - Gradient Flow[/]")
console.newline()

directions = [
    (Direction.VERTICAL, "Top to bottom"),
    (Direction.HORIZONTAL, "Left to right"),
    (Direction.DIAGONAL, "Corner to corner"),
]

for direction, description in directions:
    effect = EffectSpec.gradient("cyan", "magenta", direction=direction)
    console.frame(
        description,
        title=f"Direction.{direction.name}",
        effect=effect,
        border=Border.DOUBLE,
        width=40,
    )

console.newline()

# =============================================================================
# 4. Target Enum - What to colorize
# =============================================================================

console.rule("[cyan]4. Target Enum - Effect Application[/]")
console.newline()

targets = [
    (Target.BORDER, "Border only"),
    (Target.CONTENT, "Content only"),
    (Target.BOTH, "Border + Content"),
]

for target, description in targets:
    effect = EffectSpec.gradient("gold", "orange", target=target)
    console.frame(
        description,
        title=f"Target.{target.name}",
        effect=effect,
        border=Border.HEAVY,
        width=35,
    )

console.newline()

# =============================================================================
# 5. Align Enum - Text alignment
# =============================================================================

console.rule("[cyan]5. Align Enum - Text Positioning[/]")
console.newline()

alignments = [
    (Align.LEFT, "Left aligned text"),
    (Align.CENTER, "Center aligned text"),
    (Align.RIGHT, "Right aligned text"),
]

for align, text in alignments:
    console.frame(
        text,
        title=f"Align.{align.name}",
        align=align,  # Using enum!
        border=Border.ROUNDED,
        effect=Effect.OCEAN,
        width=45,
    )

console.newline()

# =============================================================================
# 6. LayoutMode Enum - Layout arrangements
# =============================================================================

console.rule("[cyan]6. LayoutMode Enum - Arrangements[/]")
console.newline()

console.text("[bold]Layout modes for frame_group():[/]")
console.text(f"  - LayoutMode.VERTICAL   = '{LayoutMode.VERTICAL}'")
console.text(f"  - LayoutMode.HORIZONTAL = '{LayoutMode.HORIZONTAL}'")
console.text(f"  - LayoutMode.GRID       = '{LayoutMode.GRID}'")
console.newline()

# Demonstrate grid layout
items = [
    {"title": "CPU", "content": "45%", "effect": Effect.SUCCESS},
    {"title": "Memory", "content": "72%", "effect": Effect.WARNING},
    {"title": "Disk", "content": "23%", "effect": Effect.SUCCESS},
    {"title": "Network", "content": "Active", "effect": Effect.INFO},
]

console.frame_group(
    [
        {"title": item["title"], "content": item["content"], "effect": item["effect"]}
        for item in items
    ],
    layout=LayoutMode.GRID,  # Using enum!
    columns=2,
    item_width=30,
)
console.newline()

# =============================================================================
# 7. Combining Enums - Real-world example
# =============================================================================

console.rule("[cyan]7. Combining Enums - Complete Example[/]")
console.newline()

# A complete example using multiple enums together
console.frame(
    [
        "Deployment Status",
        "",
        "  API Server:    Online",
        "  Database:      Connected",
        "  Cache:         Healthy",
        "",
        "All systems operational",
    ],
    title="Production",
    border=Border.DOUBLE,           # Border enum
    align=Align.LEFT,               # Align enum
    effect=EffectSpec.gradient(
        "green", "cyan",
        direction=Direction.DIAGONAL,  # Direction enum
        target=Target.BORDER,          # Target enum
    ),
    width=40,
)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    [
        "Enum Benefits:",
        "",
        "  1. IDE autocomplete for all options",
        "  2. Type checking catches typos",
        "  3. Self-documenting code",
        "  4. Backward compatible with strings",
        "",
        "Usage:",
        '  border=Border.ROUNDED    # Same as "rounded"',
        '  effect=Effect.OCEAN      # Same as "ocean"',
        '  align=Align.CENTER       # Same as "center"',
    ],
    title="Summary",
    effect=Effect.INFO,
    border=Border.ROUNDED,
)
