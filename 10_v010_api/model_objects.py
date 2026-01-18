#!/usr/bin/env python3
"""Model Objects Example - v0.10.0 API.

Demonstrates using the Model layer directly to construct immutable
ConsoleObjects with full type safety and serialization support.

The Model layer provides:
- Immutable dataclasses (frozen=True)
- Type-safe construction
- JSON/dict serialization via to_dict()/from_dict()
- Recursive nesting support

Usage:
    python 10_v010_api/model_objects.py
"""

from styledconsole import (
    Console,
    FrameModel,
    Group,
    Layout,
    RuleModel,
    Spacer,
    Style,
    Text,
    icons,
)

console = Console()

console.text("[bold cyan]Model Layer Demo - v0.10.0 API[/]")
console.text("[dim]Direct construction of immutable ConsoleObjects[/]")
console.newline()

# =============================================================================
# Basic Text Object
# =============================================================================

console.rule("[yellow]1. Text Objects with Styles[/]")
console.newline()

# Create styled text using model objects
plain_text = Text(content="Plain text without styling")
styled_text = Text(
    content="Styled text with bold and color",
    style=Style(bold=True, color="cyan"),
)

console.render_object(plain_text)
console.render_object(styled_text)
console.newline()

# =============================================================================
# Frame Objects
# =============================================================================

console.rule("[yellow]2. Frame Objects[/]")
console.newline()

# Simple frame
simple_frame = FrameModel(
    content=Text(content="Simple frame content"),
    title="Simple Frame",
    border="rounded",
)
console.render_object(simple_frame)
console.newline()

# Frame with effect
gradient_frame = FrameModel(
    content=Text(content=f"{icons.SPARKLES} Frame with gradient effect"),
    title="Gradient Frame",
    border="heavy",
    effect="ocean",
)
console.render_object(gradient_frame)
console.newline()

# =============================================================================
# Layout Objects
# =============================================================================

console.rule("[yellow]3. Layout Objects[/]")
console.newline()

# Vertical layout with children
vertical_layout = Layout(
    direction="vertical",
    gap=1,
    children=(
        Text(content=f"{icons.CHECK_MARK_BUTTON} First item", style=Style(color="green")),
        Text(content=f"{icons.CHECK_MARK_BUTTON} Second item", style=Style(color="green")),
        Text(content=f"{icons.CHECK_MARK_BUTTON} Third item", style=Style(color="green")),
    ),
)
console.render_object(vertical_layout)
console.newline()

# =============================================================================
# Complex Nested Structure
# =============================================================================

console.rule("[yellow]4. Complex Nested Structure[/]")
console.newline()

# Build a dashboard-like structure using pure model objects
dashboard = Layout(
    direction="vertical",
    gap=1,
    children=(
        # Header
        FrameModel(
            content=Text(content="System Dashboard", style=Style(bold=True)),
            border="double",
            effect="sunset",
        ),
        # Spacer
        Spacer(lines=1),
        # Status section
        Group(
            children=(
                Text(
                    content=f"{icons.GEAR} Status: Online",
                    style=Style(color="green"),
                ),
                Text(
                    content=f"{icons.SATELLITE_ANTENNA} Signal: Strong",
                    style=Style(color="cyan"),
                ),
            ),
        ),
        # Rule
        RuleModel(title="Details", style=Style(dim=True, color="white")),
        # Info frame
        FrameModel(
            content=Text(content="CPU: 45%  |  Memory: 8GB  |  Disk: 120GB"),
            title="Resources",
            border="rounded",
        ),
    ),
)

console.render_object(dashboard)
console.newline()

# =============================================================================
# Serialization
# =============================================================================

console.rule("[yellow]5. Serialization Demo[/]")
console.newline()

# Models can be serialized to dict
sample_frame = FrameModel(
    content=Text(content="Serializable content"),
    title="Serializable",
    effect="fire",
)

# Convert to dict
frame_dict = sample_frame.to_dict()
console.text(f"[bold]Serialized to dict:[/]")
console.text(f"  type: {frame_dict.get('type')}")
console.text(f"  title: {frame_dict.get('title')}")
console.text(f"  effect: {frame_dict.get('effect')}")
console.newline()

# Recreate from dict
reconstructed = FrameModel.from_dict(frame_dict)
console.text("[bold]Reconstructed from dict:[/]")
console.render_object(reconstructed)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
[bold cyan]Model Layer Benefits:[/]

{icons.SPARKLES} Immutable objects - safe to share and cache
{icons.SPARKLES} Type-safe construction with IDE support
{icons.SPARKLES} Serialization via to_dict()/from_dict()
{icons.SPARKLES} Recursive nesting for complex layouts
{icons.SPARKLES} Separation of data from rendering
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=1,
)
