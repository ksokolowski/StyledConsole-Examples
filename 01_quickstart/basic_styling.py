#!/usr/bin/env python3
"""Basic Styling - Colors, borders, and icons.

Learn the fundamentals of styling in StyledConsole:
- Border styles (8 built-in options)
- Colors (CSS4 names, hex, RGB)
- Icons (with automatic ASCII fallback)

Usage:
    python 01_quickstart/basic_styling.py
"""

from styledconsole import Console, icons

console = Console()

# =============================================================================
# Border Styles
# =============================================================================

console.rule("Border Styles")
console.newline()

console.frame("Solid border (default)", border="solid")
console.frame("Rounded corners", border="rounded")
console.frame("Double lines", border="double")
console.frame("Heavy/thick lines", border="heavy")

console.newline()

# =============================================================================
# Colors
# =============================================================================

console.rule("Colors")
console.newline()

# CSS4 color names
console.frame("CSS4 color: dodgerblue", border_color="dodgerblue")
console.frame("CSS4 color: coral", border_color="coral")

# Hex colors
console.frame("Hex color: #ff6b6b", border_color="#ff6b6b")

# Semantic colors (from theme)
console.frame("Success message!", border_color="green", title="Success")
console.frame("Warning message!", border_color="orange", title="Warning")
console.frame("Error message!", border_color="red", title="Error")

console.newline()

# =============================================================================
# Icons
# =============================================================================

console.rule("Icons")
console.newline()

# Icons automatically fall back to ASCII in limited terminals
console.frame(
    f"""
{icons.CHECK_MARK_BUTTON} Task completed successfully
{icons.CROSS_MARK} Task failed
{icons.WARNING} Warning detected
{icons.ROCKET} Deployment started
{icons.FIRE} Hot feature!
{icons.SPARKLES} New and shiny
    """.strip(),
    title="Status Icons",
    border="rounded",
    border_color="cyan",
)

console.newline()

# =============================================================================
# Combining Everything
# =============================================================================

console.rule("Putting It Together")
console.newline()

console.frame(
    f"""
{icons.CHECK_MARK_BUTTON} Database connected
{icons.CHECK_MARK_BUTTON} Cache initialized
{icons.CHECK_MARK_BUTTON} API routes loaded
{icons.ROCKET} Server ready on port 8080
    """.strip(),
    title=f"{icons.SPARKLES} Startup Complete",
    border="double",
    border_color="lime",
)
