#!/usr/bin/env python3
"""Builder Pattern Example - v0.10.0 API.

Demonstrates the fluent Builder API for constructing ConsoleObjects
with method chaining and validation.

The Builder layer provides:
- Fluent interface with method chaining
- Validation before build()
- Direct render() when bound to Console
- Type-safe construction

Usage:
    python 10_v010_api/builder_pattern.py
"""

from styledconsole import (
    BannerBuilder,
    Console,
    FrameBuilder,
    LayoutBuilder,
    TableBuilder,
    icons,
)

console = Console()

console.text("[bold cyan]Builder Pattern Demo - v0.10.0 API[/]")
console.text("[dim]Fluent API with method chaining[/]")
console.newline()

# =============================================================================
# FrameBuilder - Basic Usage
# =============================================================================

console.rule("[yellow]1. FrameBuilder - Basic Usage[/]")
console.newline()

# Build a frame step by step
frame = (
    FrameBuilder()
    .content("Hello from the Builder API!")
    .title("FrameBuilder")
    .border("rounded")
    .build()
)
console.render_object(frame)
console.newline()

# =============================================================================
# FrameBuilder - With Effects and Styling
# =============================================================================

console.rule("[yellow]2. FrameBuilder - With Effects[/]")
console.newline()

styled_frame = (
    FrameBuilder()
    .content(f"{icons.ROCKET} Mission Control Active")
    .title("Status")
    .subtitle("Real-time")
    .border("heavy")
    .effect("ocean")
    .padding(1)
    .build()
)
console.render_object(styled_frame)
console.newline()

# =============================================================================
# Console Factory Methods
# =============================================================================

console.rule("[yellow]3. Console Factory Methods[/]")
console.newline()

# Console provides factory methods that bind builders automatically
# This allows direct render() calls

# Build and render in one chain
console.build_frame().content("Built via console factory").title("Factory").border("rounded").render()
console.newline()

# Or build first, then render
banner_obj = (
    console.build_banner()
    .text("DEMO")
    .font("slant")
    .effect("fire")
    .build()
)
console.render_object(banner_obj)
console.newline()

# =============================================================================
# TableBuilder
# =============================================================================

console.rule("[yellow]4. TableBuilder[/]")
console.newline()

table = (
    TableBuilder()
    .title("System Metrics")
    .columns("Metric", "Value", "Status")
    .add_row("CPU", "45%", f"{icons.CHECK_MARK_BUTTON}")
    .add_row("Memory", "8GB", f"{icons.CHECK_MARK_BUTTON}")
    .add_row("Disk", "78%", f"{icons.WARNING}")
    .effect("steel")
    .build()
)
console.render_object(table)
console.newline()

# =============================================================================
# LayoutBuilder
# =============================================================================

console.rule("[yellow]5. LayoutBuilder[/]")
console.newline()

# Build a vertical layout with ConsoleObjects
from styledconsole import FrameModel, Style, Text

layout = (
    LayoutBuilder()
    .vertical()
    .gap(1)
    .add(
        Text(content="First section", style=Style(bold=True, color="cyan")),
        FrameBuilder().content("Content in a frame").title("Section 1").border("rounded").build(),
        Text(content="Second section", style=Style(bold=True, color="cyan")),
        FrameBuilder().content("More content here").title("Section 2").border("rounded").build(),
    )
    .build()
)
console.render_object(layout)
console.newline()

# =============================================================================
# BannerBuilder
# =============================================================================

console.rule("[yellow]6. BannerBuilder[/]")
console.newline()

banner = (
    BannerBuilder()
    .text("HELLO")
    .font("small")
    .effect("rainbow")
    .build()
)
console.render_object(banner)
console.newline()

# =============================================================================
# Chained Workflow
# =============================================================================

console.rule("[yellow]7. Complete Workflow[/]")
console.newline()

# Build everything in one chain and render directly
(
    console.build_frame()
    .content(
        f"""
{icons.SPARKLES} Builder Pattern Benefits:

  - Fluent API with IntelliSense support
  - Step-by-step construction
  - Validation at build time
  - Direct render() from Console factories
  - Clean, readable code
        """.strip()
    )
    .title("Summary")
    .border("rounded_thick")
    .effect("aurora")
    .padding(1)
    .render()
)
