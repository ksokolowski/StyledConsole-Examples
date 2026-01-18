#!/usr/bin/env python3
"""Template System Example - v0.10.0 API.

Demonstrates the template system for reusable UI patterns
with variable substitution and built-in templates.

The Template system provides:
- Built-in templates (info_box, error_box, warning_box, etc.)
- Custom template registration
- Variable substitution with ${name:default} syntax
- Template inheritance and composition

Usage:
    python 10_v010_api/templates.py
"""

from styledconsole import (
    BUILTIN_TEMPLATES,
    Console,
    Declarative,
    Template,
    from_template,
    icons,
)

console = Console()

console.text("[bold cyan]Template System Demo - v0.10.0 API[/]")
console.text("[dim]Reusable UI patterns with variables[/]")
console.newline()

# =============================================================================
# Built-in Templates
# =============================================================================

console.rule("[yellow]1. Built-in Templates[/]")
console.newline()

# List available templates
console.text("[bold]Available built-in templates:[/]")
for name in sorted(BUILTIN_TEMPLATES.keys()):
    console.text(f"  - {name}")
console.newline()

# Use info_box template
console.render_template("info_box", message="This is an informational message")
console.newline()

# Use warning_box template
console.render_template("warning_box", message="This is a warning message")
console.newline()

# Use error_box template
console.render_template("error_box", message="This is an error message")
console.newline()

# =============================================================================
# Custom Templates
# =============================================================================

console.rule("[yellow]2. Custom Templates[/]")
console.newline()

# Create a Declarative instance for custom templates
decl = Declarative()

# Register a custom template
decl.register_template(
    "status_panel",
    {
        "type": "frame",
        "title": "${title:System Status}",
        "content": {
            "type": "layout",
            "direction": "vertical",
            "children": [
                {"type": "text", "content": "${status_line}"},
                {"type": "text", "content": "${details:No additional details}"},
            ],
        },
        "effect": "${effect:steel}",
        "border": "rounded",
    },
)

# Use the custom template
obj = decl.from_template(
    "status_panel",
    title="Server Status",
    status_line=f"{icons.CHECK_MARK_BUTTON} All systems operational",
    details=f"{icons.GEAR} Last check: 10 seconds ago",
    effect="ocean",
)
console.render_object(obj)
console.newline()

# Use with defaults
obj2 = decl.from_template(
    "status_panel",
    status_line=f"{icons.WARNING} Degraded performance",
)
console.render_object(obj2)
console.newline()

# =============================================================================
# Template Object API
# =============================================================================

console.rule("[yellow]3. Template Object API[/]")
console.newline()

# Create a Template directly
notification_template = Template(
    definition={
        "type": "frame",
        "title": "${icon} ${title}",
        "content": {"type": "text", "content": "${message}"},
        "effect": "${effect:fire}",
        "border": "heavy",
    },
    name="notification",
)

# Render the template
rendered_dict = notification_template.render(
    icon=str(icons.WARNING),
    title="Alert",
    message="System temperature is high",
)
console.text("[bold]Rendered template dict:[/]")
console.text(f"  title: {rendered_dict.get('title')}")
console.text(f"  effect: {rendered_dict.get('effect')}")
console.newline()

# Convert to object and display
from styledconsole.model.registry import create_object

obj = create_object(rendered_dict)
console.render_object(obj)
console.newline()

# =============================================================================
# Dashboard Template
# =============================================================================

console.rule("[yellow]4. Dashboard Template[/]")
console.newline()

# Register a more complex dashboard template
decl.register_template(
    "dashboard_header",
    {
        "type": "layout",
        "direction": "vertical",
        "gap": 1,
        "children": [
            {"banner": "${app_name}", "font": "small", "effect": "${banner_effect:rainbow}"},
            {
                "type": "frame",
                "title": "${subtitle:Dashboard}",
                "content": {"type": "text", "content": "${description}"},
                "effect": "${frame_effect:ocean}",
                "border": "rounded",
            },
        ],
    },
)

# Use the dashboard template
dashboard = decl.from_template(
    "dashboard_header",
    app_name="MYAPP",
    subtitle="Control Center",
    description=f"{icons.GEAR} Managing 5 services | {icons.HIGH_VOLTAGE} Power: 98%",
    banner_effect="fire",
)
console.render_object(dashboard)
console.newline()

# =============================================================================
# From Template Function
# =============================================================================

console.rule("[yellow]5. from_template Function[/]")
console.newline()

# Use the standalone from_template function for built-in templates
success_obj = from_template("success_box", message="Operation completed successfully!")
console.render_object(success_obj)
console.newline()

# =============================================================================
# Template Composition
# =============================================================================

console.rule("[yellow]6. Template Composition[/]")
console.newline()

# Templates can reference other structures
decl.register_template(
    "app_layout",
    {
        "column": [
            {"banner": "${title}", "font": "small"},
            {"type": "spacer", "lines": 1},
            {
                "frame": "${content}",
                "title": "${section:Main}",
                "effect": "${effect:steel}",
            },
            {"type": "spacer", "lines": 1},
            {"type": "text", "content": "${footer:Created with StyledConsole}"},
        ],
        "gap": 0,
    },
)

app = decl.from_template(
    "app_layout",
    title="DEMO",
    content=f"{icons.SPARKLES} Template composition in action!",
    section="Features",
    effect="aurora",
)
console.render_object(app)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
[bold cyan]Template System Benefits:[/]

{icons.SPARKLES} Built-in templates for common patterns
{icons.SPARKLES} Custom template registration
{icons.SPARKLES} Variable substitution with defaults
{icons.SPARKLES} Reusable UI components
{icons.SPARKLES} Clean separation of structure and data
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=1,
)
