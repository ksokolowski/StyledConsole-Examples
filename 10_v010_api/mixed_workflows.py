#!/usr/bin/env python3
"""Mixed Workflows Example - v0.10.0 API.

Demonstrates mixing different API layers together for maximum
flexibility and code clarity.

You can freely combine:
- Classic Console methods (console.frame(), console.banner())
- Model objects (Text, Frame, Layout)
- Builder API (FrameBuilder, TableBuilder)
- Declarative syntax (dict/list definitions)

Usage:
    python 10_v010_api/mixed_workflows.py
"""

from styledconsole import (
    Console,
    FrameBuilder,
    FrameModel,
    Layout,
    Style,
    Text,
    icons,
    load_dict,
)

console = Console()

console.text("[bold cyan]Mixed Workflows Demo - v0.10.0 API[/]")
console.text("[dim]Combining different API layers[/]")
console.newline()

# =============================================================================
# Workflow 1: Builder + Model
# =============================================================================

console.rule("[yellow]1. Builder + Model[/]")
console.newline()

# Create a frame using builder
header_frame = (
    FrameBuilder()
    .content("Dashboard Header")
    .title("Header")
    .effect("ocean")
    .build()
)

# Create text using model
status_text = Text(
    content=f"{icons.CHECK_MARK_BUTTON} All systems operational",
    style=Style(color="green"),
)

# Combine in a Layout
combined = Layout(
    direction="vertical",
    gap=1,
    children=(header_frame, status_text),
)

console.render_object(combined)
console.newline()

# =============================================================================
# Workflow 2: Declarative + Model
# =============================================================================

console.rule("[yellow]2. Declarative + Model[/]")
console.newline()

# Create a frame declaratively
decl_frame = load_dict({
    "frame": "From declarative API",
    "title": "Declarative",
    "effect": "fire",
})

# Create text with model
model_text = Text(
    content=f"{icons.SPARKLES} From model API",
    style=Style(bold=True, color="cyan"),
)

# Combine both
mixed_layout = Layout(
    direction="vertical",
    gap=1,
    children=(decl_frame, model_text),
)

console.render_object(mixed_layout)
console.newline()

# =============================================================================
# Workflow 3: Classic + New APIs
# =============================================================================

console.rule("[yellow]3. Classic API + New APIs[/]")
console.newline()

# Use classic console methods
console.frame("Classic console.frame() call", title="Classic", border="rounded")

# Build with builder and render via console
frame_obj = (
    console.build_frame()
    .content("Builder API via Console factory")
    .title("Builder")
    .border("rounded")
    .effect("steel")
    .build()
)
console.render_object(frame_obj)

# Render declarative directly
console.render_dict({
    "frame": "Declarative via console.render_dict()",
    "title": "Declarative",
    "border": "rounded",
    "effect": "sunset",
})
console.newline()

# =============================================================================
# Workflow 4: Building Complex Dashboards
# =============================================================================

console.rule("[yellow]4. Complex Dashboard Workflow[/]")
console.newline()

# Step 1: Create header with builder
header = (
    console.build_banner()
    .text("MONITOR")
    .font("small")
    .effect("rainbow")
    .build()
)

# Step 2: Create status panels with model
status_panel = FrameModel(
    content=Text(
        content=f"""
{icons.GEAR} CPU: 45%
{icons.HIGH_VOLTAGE} Memory: 8GB
{icons.SATELLITE_ANTENNA} Network: Active
        """.strip()
    ),
    title="System Status",
    border="rounded",
    effect="ocean",
)

# Step 3: Create alerts with declarative
alerts_data = {
    "frame": [
        f"{icons.WARNING} High memory usage on server-02",
        f"{icons.CHECK_MARK_BUTTON} Backup completed successfully",
    ],
    "title": "Recent Alerts",
    "effect": "fire",
}
alerts_panel = load_dict(alerts_data)

# Step 4: Combine all into final layout
dashboard = Layout(
    direction="vertical",
    gap=1,
    children=(header, status_panel, alerts_panel),
)

console.render_object(dashboard)
console.newline()

# =============================================================================
# Workflow 5: Data-Driven UI
# =============================================================================

console.rule("[yellow]5. Data-Driven UI[/]")
console.newline()

# Simulate data from an API or config
config = {
    "services": [
        {"name": "web-server", "status": "running", "cpu": 23},
        {"name": "database", "status": "running", "cpu": 45},
        {"name": "cache", "status": "stopped", "cpu": 0},
    ],
}

# Build UI dynamically from data
service_items = []
for svc in config["services"]:
    icon = icons.CHECK_MARK_BUTTON if svc["status"] == "running" else icons.CROSS_MARK
    color = "green" if svc["status"] == "running" else "red"
    service_items.append(
        Text(
            content=f"{icon} {svc['name']}: {svc['status']} (CPU: {svc['cpu']}%)",
            style=Style(color=color),
        )
    )

# Wrap in frame
services_frame = FrameModel(
    content=Layout(direction="vertical", children=tuple(service_items)),
    title="Services",
    border="rounded",
    effect="steel",
)

console.render_object(services_frame)
console.newline()

# =============================================================================
# Workflow 6: Reusable Components
# =============================================================================

console.rule("[yellow]6. Reusable Components[/]")
console.newline()


def create_status_card(title: str, status: str, details: str) -> FrameModel:
    """Create a reusable status card component."""
    icon = icons.CHECK_MARK_BUTTON if status == "ok" else icons.WARNING
    color = "green" if status == "ok" else "yellow"
    effect = "ocean" if status == "ok" else "fire"

    return FrameModel(
        content=Layout(
            direction="vertical",
            children=(
                Text(content=f"{icon} {status.upper()}", style=Style(bold=True, color=color)),
                Text(content=details),
            ),
        ),
        title=title,
        border="rounded",
        effect=effect,
    )


# Create multiple cards
card1 = create_status_card("API Server", "ok", "Response time: 45ms")
card2 = create_status_card("Database", "warning", "High connection count")

# Layout cards
cards_layout = Layout(direction="vertical", gap=1, children=(card1, card2))
console.render_object(cards_layout)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
[bold cyan]Mixed Workflow Benefits:[/]

{icons.SPARKLES} Use classic API for quick prototyping
{icons.SPARKLES} Use Model for type-safe, immutable structures
{icons.SPARKLES} Use Builder for fluent, readable construction
{icons.SPARKLES} Use Declarative for config-driven UIs
{icons.SPARKLES} Mix freely - all APIs are interoperable!
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=1,
)
