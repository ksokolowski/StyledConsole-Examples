#!/usr/bin/env python3
"""Declarative Syntax Example - v0.10.0 API.

Demonstrates the declarative/shorthand syntax for defining
UI components using dictionaries and lists.

The Declarative layer provides:
- JSON/YAML-like definition of UIs
- Shorthand syntax ("Hello" -> Text, {"frame": "x"} -> Frame)
- List-based layouts (["a", "b"] -> vertical Layout)
- Template variables (${name:default})

Usage:
    python 10_v010_api/declarative_syntax.py
"""

from styledconsole import Console, icons, load_dict, normalize

console = Console()

console.text("[bold cyan]Declarative Syntax Demo - v0.10.0 API[/]")
console.text("[dim]JSON-like definitions with shorthand support[/]")
console.newline()

# =============================================================================
# Simple String -> Text
# =============================================================================

console.rule("[yellow]1. String Shorthand[/]")
console.newline()

# A simple string becomes a Text object
console.render_dict("Hello from declarative syntax!")
console.newline()

# =============================================================================
# List -> Vertical Layout
# =============================================================================

console.rule("[yellow]2. List Shorthand[/]")
console.newline()

# A list becomes a vertical layout
console.render_dict([
    f"{icons.CHECK_MARK_BUTTON} First item",
    f"{icons.CHECK_MARK_BUTTON} Second item",
    f"{icons.CHECK_MARK_BUTTON} Third item",
])
console.newline()

# =============================================================================
# Dict Shorthand -> Frame
# =============================================================================

console.rule("[yellow]3. Frame Shorthand[/]")
console.newline()

# {"frame": "content"} becomes a Frame
console.render_dict({
    "frame": "[bold green]Success![/] This content has [italic]markup[/].",
    "title": "[yellow]Frame Shorthand[/]",
    "border": "rounded",
})
console.newline()

# With effect
console.render_dict({
    "frame": f"{icons.ROCKET} Content with effect",
    "title": "Styled Frame",
    "effect": "ocean",
})
console.newline()

# =============================================================================
# Dict Shorthand -> Banner
# =============================================================================

console.rule("[yellow]4. Banner Shorthand[/]")
console.newline()

console.render_dict({
    "banner": "DEMO",
    "font": "small",
    "effect": "fire",
})
console.newline()

# =============================================================================
# Row/Column Layouts
# =============================================================================

console.rule("[yellow]5. Row and Column Layouts[/]")
console.newline()

# Vertical column layout
console.render_dict({
    "column": [
        {"frame": "Top Panel", "title": "A", "border": "rounded"},
        {"frame": "Bottom Panel", "title": "B", "border": "rounded"},
    ],
    "gap": 1,
})
console.newline()

# =============================================================================
# Complex Nested Structure
# =============================================================================

console.rule("[yellow]6. Complex Nested Structure[/]")
console.newline()

dashboard = {
    "column": [
        # Header banner
        {"banner": "APP", "font": "slant", "effect": "rainbow"},
        # Status section
        {
            "frame": [
                f"{icons.GEAR} Status: Online",
                f"{icons.HIGH_VOLTAGE} Power: 100%",
                f"{icons.SATELLITE_ANTENNA} Signal: Strong",
            ],
            "title": "System Status",
            "effect": "ocean",
        },
        # Spacer (using explicit type)
        {"type": "spacer", "lines": 1},
        # Info text
        "Ready for operations",
    ],
    "gap": 1,
}

console.render_dict(dashboard)
console.newline()

# =============================================================================
# Template Variables
# =============================================================================

console.rule("[yellow]7. Template Variables[/]")
console.newline()

# Define a template with variables
template = {
    "frame": "${message}",
    "title": "${title:Default Title}",
    "effect": "${effect:steel}",
}

# Render with variables
console.render_dict(template, variables={
    "message": "Hello with variables!",
    "title": "Custom Title",
})
console.newline()

# Render with different variables (uses default for effect)
console.render_dict(template, variables={
    "message": "Using default effect",
    "title": "Another Title",
})
console.newline()

# =============================================================================
# Normalize Function
# =============================================================================

console.rule("[yellow]8. Normalize Function[/]")
console.newline()

# See what shorthand expands to
shorthand = {"frame": "Hello", "title": "Test"}
normalized = normalize(shorthand)

console.text("[bold]Shorthand input:[/]")
console.text(f"  {shorthand}")
console.newline()
console.text("[bold]Normalized output:[/]")
console.text(f"  type: {normalized.get('type')}")
console.text(f"  content: {normalized.get('content')}")
console.text(f"  title: {normalized.get('title')}")
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
[bold cyan]Declarative Syntax Benefits:[/]

{icons.SPARKLES} "string" -> Text object
{icons.SPARKLES} ["a", "b"] -> vertical Layout
{icons.SPARKLES} {{"frame": "x"}} -> Frame with content
{icons.SPARKLES} {{"banner": "x"}} -> Banner with text
{icons.SPARKLES} {{"column": [...]}} -> vertical Layout
{icons.SPARKLES} {{"row": [...]}} -> horizontal Layout
{icons.SPARKLES} ${{name:default}} -> variable substitution
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=1,
)
