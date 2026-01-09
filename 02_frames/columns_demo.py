#!/usr/bin/env python3
"""StyledColumns Example - Multi-column layouts with automatic policy awareness.

StyledColumns extends Rich's Columns with policy-aware rendering,
automatic emoji sanitization, and VS16 emoji width fix.

Usage:
    python 02_frames/columns_demo.py
"""

from styledconsole import Console, EffectSpec, StyledColumns, icons

console = Console()

console.banner("COLUMNS", font="small", effect=EffectSpec.gradient("cyan", "blue"))
console.newline()

# =============================================================================
# Basic Columns Layout
# =============================================================================

console.rule("Basic Columns")
console.newline()

items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
console.columns(items, padding=(0, 2))
console.newline()

# =============================================================================
# With Icons and Emoji
# =============================================================================

console.rule("With Icons")
console.newline()

status_items = [
    f"{icons.CHECK_MARK_BUTTON} Task Complete",
    f"{icons.WARNING} Low Memory",
    f"{icons.CROSS_MARK} Failed",
    f"{icons.GEAR} Processing",
    f"{icons.SPARKLES} Success",
]
console.columns(status_items, padding=(0, 3))
console.newline()

# =============================================================================
# Equal Width Columns
# =============================================================================

console.rule("Equal Width Columns")
console.newline()

mixed_items = [
    "Short",
    "Medium Length",
    "Very Long Item Name Here",
    "XS",
]
console.columns(mixed_items, padding=(0, 2), equal=True)
console.newline()

# =============================================================================
# Column-First (Vertical) Filling
# =============================================================================

console.rule("Column-First Filling")
console.newline()

console.text("Normal (horizontal):", bold=True)
console.columns([f"Item {i}" for i in range(1, 9)], padding=(0, 2))
console.newline()

console.text("Column-first (vertical):", bold=True)
console.columns([f"Item {i}" for i in range(1, 9)], padding=(0, 2), column_first=True)
console.newline()

# =============================================================================
# Expand to Fill Width
# =============================================================================

console.rule("Expand to Fill Width")
console.newline()

console.text("Normal:", bold=True)
console.columns(["Left", "Middle", "Right"], padding=(0, 2))
console.newline()

console.text("Expanded:", bold=True)
console.columns(["Left", "Middle", "Right"], padding=(0, 2), expand=True)
console.newline()

# =============================================================================
# Right-to-Left
# =============================================================================

console.rule("Right-to-Left")
console.newline()

console.text("Normal (LTR):", bold=True)
console.columns(["First", "Second", "Third"], padding=(0, 2))
console.newline()

console.text("Right-to-Left (RTL):", bold=True)
console.columns(["First", "Second", "Third"], padding=(0, 2), right_to_left=True)
console.newline()

# =============================================================================
# Using StyledColumns Directly
# =============================================================================

console.rule("Direct StyledColumns Usage")
console.newline()

# Create a StyledColumns object directly for more control
from styledconsole import RenderPolicy

# Create with custom policy (no emoji)
policy = RenderPolicy(emoji=False)
columns_obj = StyledColumns(
    [f"{icons.ROCKET} Item {i}" for i in range(1, 6)],
    padding=(0, 2),
    policy=policy,
)
console.print(columns_obj)
console.newline()

# =============================================================================
# Practical Examples
# =============================================================================

console.rule("Practical Examples")
console.newline()

# File listing
console.text("File Listing:", bold=True, color="dodgerblue")
files = [
    f"{icons.BOOKMARK} README.md",
    f"{icons.BOOKMARK} main.py",
    f"{icons.BOOKMARK} config.json",
    f"{icons.BOOKMARK} test.py",
    f"{icons.BOOKMARK} utils.py",
    f"{icons.BOOKMARK} data.csv",
]
console.columns(files, padding=(0, 2))
console.newline()

# Dashboard widgets
console.text("Dashboard Metrics:", bold=True, color="dodgerblue")
metrics = [
    f"{icons.CHECK_MARK_BUTTON} CPU: 45%",
    f"{icons.WARNING} Memory: 78%",
    f"{icons.CHECK_MARK_BUTTON} Disk: 32%",
    f"{icons.CROSS_MARK} Network: Down",
]
console.columns(metrics, padding=(0, 3), equal=True)
console.newline()

# Color palette
console.text("Color Palette:", bold=True, color="dodgerblue")
colors = [
    "[red]Red[/]",
    "[green]Green[/]",
    "[blue]Blue[/]",
    "[yellow]Yellow[/]",
    "[magenta]Magenta[/]",
    "[cyan]Cyan[/]",
]
console.columns(colors, padding=(0, 2))
console.newline()

console.frame(
    f"""
{icons.SPARKLES} Policy-Aware: Auto-converts emoji when policy.emoji=False
{icons.SPARKLES} VS16 Fix: Proper alignment with emoji like ☁️ ⚙️
{icons.SPARKLES} Rich Integration: All Rich renderables supported
{icons.SPARKLES} Flexible: Equal width, expand, RTL, column-first
    """.strip(),
    title="StyledColumns Features",
    border="rounded",
    border_color="dodgerblue",
)
