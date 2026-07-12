#!/usr/bin/env python3
"""Migration Guide - Classic API to v0.10.0 API.

This guide demonstrates how to migrate from the classic Console API
to the new v0.10.0 declarative and builder APIs.

Both APIs will continue to work - the classic API is not deprecated.
The new APIs provide additional flexibility and patterns.

Usage:
    python 10_v010_api/migration_guide.py
"""

from styledconsole import (
    # Classic API
    Console,
    icons,
    # v0.10.0 Model API
    FrameModel,
    Layout,
    Style,
    Text,
    # v0.10.0 Builder API
    FrameBuilder,
    LayoutBuilder,
    TableBuilder,
    # v0.10.0 Declarative API
    from_template,
    load_dict,
    render_jinja,
)

console = Console()

console.text("[bold cyan]Migration Guide - Classic to v0.10.0 API[/]")
console.text("[dim]Both APIs work together - choose based on your needs[/]")
console.newline()

# =============================================================================
# 1. Simple Frame - Classic vs New APIs
# =============================================================================

console.rule("[yellow]1. Simple Frame[/]")
console.newline()

# CLASSIC: Direct console method
console.text("[bold]Classic API:[/]")
console.frame("Hello World!", title="Classic", border="rounded")
console.newline()

# NEW: Builder API
console.text("[bold]Builder API:[/]")
frame = FrameBuilder().content("Hello World!").title("Builder").border("rounded").build()
console.render_object(frame)
console.newline()

# NEW: Model API
console.text("[bold]Model API:[/]")
frame = FrameModel(
    content=Text(content="Hello World!"),
    title="Model",
    border="rounded",
)
console.render_object(frame)
console.newline()

# NEW: Declarative API
console.text("[bold]Declarative API:[/]")
console.render_dict({"frame": "Hello World!", "title": "Declarative", "border": "rounded"})
console.newline()

# =============================================================================
# 2. Styled Content
# =============================================================================

console.rule("[yellow]2. Styled Content[/]")
console.newline()

# CLASSIC: Inline Rich markup
console.text("[bold]Classic (Rich markup):[/]")
console.frame("[bold cyan]Styled[/] [green]content[/]", title="Classic")
console.newline()

# NEW: Model with Style object
console.text("[bold]Model with Style:[/]")
styled_text = Text(content="Styled content", style=Style(bold=True, color="cyan"))
frame = FrameModel(content=styled_text, title="Model")
console.render_object(frame)
console.newline()

# =============================================================================
# 3. Effects and Gradients
# =============================================================================

console.rule("[yellow]3. Effects and Gradients[/]")
console.newline()

# CLASSIC: effect parameter
console.text("[bold]Classic:[/]")
console.frame("Ocean effect", title="Classic", effect="ocean")
console.newline()

# NEW: Same parameter works in all APIs
console.text("[bold]Builder:[/]")
frame = FrameBuilder().content("Ocean effect").title("Builder").effect("ocean").build()
console.render_object(frame)
console.newline()

console.text("[bold]Declarative:[/]")
console.render_dict({"frame": "Ocean effect", "title": "Declarative", "effect": "ocean"})
console.newline()

# =============================================================================
# 4. Multiple Frames
# =============================================================================

console.rule("[yellow]4. Multiple Frames[/]")
console.newline()

# CLASSIC: Multiple calls
console.text("[bold]Classic (multiple calls):[/]")
console.frame("First", title="A", border="rounded")
console.frame("Second", title="B", border="rounded")
console.newline()

# NEW: Layout object
console.text("[bold]Model (Layout):[/]")
layout = Layout(
    direction="vertical",
    gap=1,
    children=(
        FrameModel(content=Text(content="First"), title="A", border="rounded"),
        FrameModel(content=Text(content="Second"), title="B", border="rounded"),
    ),
)
console.render_object(layout)
console.newline()

# NEW: Declarative list
console.text("[bold]Declarative (list):[/]")
console.render_dict([
    {"frame": "First", "title": "A", "border": "rounded"},
    {"frame": "Second", "title": "B", "border": "rounded"},
])
console.newline()

# =============================================================================
# 5. Dynamic Content
# =============================================================================

console.rule("[yellow]5. Dynamic Content[/]")
console.newline()

services = [
    {"name": "api", "status": "running"},
    {"name": "db", "status": "running"},
    {"name": "cache", "status": "stopped"},
]

# CLASSIC: Python loop with console calls
console.text("[bold]Classic (loop):[/]")
for svc in services:
    icon = icons.CHECK_MARK_BUTTON if svc["status"] == "running" else icons.CROSS_MARK
    console.text(f"  {icon} {svc['name']}: {svc['status']}")
console.newline()

# NEW: Build model dynamically
console.text("[bold]Model (dynamic build):[/]")
items = []
for svc in services:
    icon = icons.CHECK_MARK_BUTTON if svc["status"] == "running" else icons.CROSS_MARK
    color = "green" if svc["status"] == "running" else "red"
    items.append(Text(content=f"{icon} {svc['name']}: {svc['status']}", style=Style(color=color)))

frame = FrameModel(
    content=Layout(direction="vertical", children=tuple(items)),
    title="Services",
    border="rounded",
)
console.render_object(frame)
console.newline()

# NEW: Jinja2 template
console.text("[bold]Jinja2 (template loop):[/]")
template = """\
type: frame
title: Services
border: rounded
content:
  type: layout
  direction: vertical
  children:
    {% for svc in services %}
    - type: text
      content: "{{ svc.status | status_icon }} {{ svc.name }}: {{ svc.status }}"
    {% endfor %}
"""
frame = render_jinja(template, services=services)
console.render_object(frame)
console.newline()

# =============================================================================
# 6. Reusable Patterns
# =============================================================================

console.rule("[yellow]6. Reusable Patterns[/]")
console.newline()

# CLASSIC: Helper function
console.text("[bold]Classic (helper function):[/]")


def show_status_classic(title: str, message: str, ok: bool) -> None:
    icon = icons.CHECK_MARK_BUTTON if ok else icons.CROSS_MARK
    effect = "ocean" if ok else "fire"
    console.frame(f"{icon} {message}", title=title, effect=effect)


show_status_classic("Status", "All systems operational", True)
console.newline()

# NEW: Built-in template
console.text("[bold]Template (built-in):[/]")
status_obj = from_template("status_card", title="Status", icon=icons.CHECK_MARK_BUTTON, status="All systems operational", effect="ocean")
console.render_object(status_obj)
console.newline()

# =============================================================================
# 7. Tables
# =============================================================================

console.rule("[yellow]7. Tables[/]")
console.newline()

# CLASSIC: rich.table.Table — shown as a listing only. Examples never
# import Rich directly (Console API rule); the code below is what you
# would migrate FROM.
console.text("[bold]Classic (Rich Table) — for comparison:[/]")
classic_code = """from rich.table import Table

table = Table(title="Users")
table.add_column("Name")
table.add_column("Role")
table.add_row("Alice", "Admin")
table.add_row("Bob", "User")
console.print(table)"""
console.frame(classic_code, title="Before: raw Rich", border="rounded")
console.newline()

# NEW: TableBuilder
console.text("[bold]Builder:[/]")
table = (
    TableBuilder()
    .title("Users")
    .columns("Name", "Role")
    .add_row("Alice", "Admin")
    .add_row("Bob", "User")
    .build()
)
console.render_object(table)
console.newline()

# =============================================================================
# 8. Choosing the Right API
# =============================================================================

console.rule("[yellow]8. When to Use Each API[/]")
console.newline()

console.render_dict({
    "type": "layout",
    "direction": "vertical",
    "gap": 1,
    "children": [
        {
            "frame": f"""{icons.SPARKLES} Classic API
  - Quick prototyping
  - Simple one-off displays
  - Interactive scripts
  - Familiar Rich-like syntax""",
            "title": "Classic console.*",
            "effect": "ocean",
        },
        {
            "frame": f"""{icons.SPARKLES} Builder API
  - Fluent method chaining
  - IDE autocompletion
  - Step-by-step construction
  - Type-safe building""",
            "title": "FrameBuilder, etc.",
            "effect": "steel",
        },
        {
            "frame": f"""{icons.SPARKLES} Model API
  - Immutable data structures
  - Serialization (to_dict/from_dict)
  - Passing objects between functions
  - Complex nested layouts""",
            "title": "FrameModel, Layout, etc.",
            "effect": "sunset",
        },
        {
            "frame": f"""{icons.SPARKLES} Declarative API
  - Config-driven UIs
  - JSON/YAML file loading
  - Template systems
  - Dynamic generation""",
            "title": "load_dict, render_jinja",
            "effect": "fire",
        },
    ],
})
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
[bold cyan]Migration Summary:[/]

{icons.CHECK_MARK_BUTTON} Classic API continues to work unchanged
{icons.CHECK_MARK_BUTTON} New APIs provide additional flexibility
{icons.CHECK_MARK_BUTTON} Mix and match - all APIs interoperate
{icons.CHECK_MARK_BUTTON} Use console.render_object() for new objects
{icons.CHECK_MARK_BUTTON} Use console.render_dict() for declarative

[bold]Key Additions in v0.10.0:[/]
  - Model layer: FrameModel, Text, Layout, etc.
  - Builders: FrameBuilder, TableBuilder, etc.
  - Declarative: load_dict, load_file, render_jinja
  - Templates: from_template, BUILTIN_TEMPLATES
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=1,
)
