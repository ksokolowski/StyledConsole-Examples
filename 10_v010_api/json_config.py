#!/usr/bin/env python3
"""JSON Configuration Example - v0.10.0 Declarative API.

Demonstrates loading UI definitions from JSON files, enabling:
- Separation of UI structure from code
- Easy theming and customization
- Non-programmer friendly configuration
- A/B testing different layouts

Usage:
    python 10_v010_api/json_config.py
"""

import json
from pathlib import Path

from styledconsole import Console, load_file, load_dict

console = Console()

console.text("[bold cyan]JSON Configuration Demo - v0.10.0 API[/]")
console.text("[dim]Load UI definitions from JSON files[/]")
console.newline()

# =============================================================================
# Create sample config files (in real apps, these would already exist)
# =============================================================================

CONFIG_DIR = Path(__file__).parent / "configs"
CONFIG_DIR.mkdir(exist_ok=True)

# App header config
app_header_config = {
    "type": "layout",
    "direction": "vertical",
    "gap": 1,
    "children": [
        {"banner": "MYAPP", "font": "small", "effect": "rainbow"},
        {
            "frame": "Welcome to MyApp - Your productivity companion",
            "title": "v2.0.0",
            "effect": "ocean",
            "border": "rounded",
        },
    ],
}

# Dashboard panels config
dashboard_config = {
    "type": "layout",
    "direction": "vertical",
    "gap": 1,
    "children": [
        {
            "frame": {
                "type": "layout",
                "direction": "vertical",
                "children": [
                    {"type": "text", "content": "CPU: ${cpu_usage}"},
                    {"type": "text", "content": "Memory: ${memory_usage}"},
                    {"type": "text", "content": "Disk: ${disk_usage}"},
                ],
            },
            "title": "System Metrics",
            "effect": "steel",
        },
        {
            "frame": "${status_message}",
            "title": "Status",
            "effect": "${status_effect}",
        },
    ],
}

# Alert templates config
alerts_config = {
    "templates": {
        "critical": {
            "frame": "${message}",
            "title": "CRITICAL",
            "effect": "fire",
            "border": "double",
        },
        "warning": {
            "frame": "${message}",
            "title": "Warning",
            "effect": "sunset",
            "border": "heavy",
        },
        "info": {
            "frame": "${message}",
            "title": "Info",
            "effect": "ocean",
            "border": "rounded",
        },
    },
}

# Menu config
menu_config = {
    "type": "frame",
    "title": "${menu_title:Main Menu}",
    "border": "rounded",
    "effect": "steel",
    "content": {
        "type": "layout",
        "direction": "vertical",
        "children": [
            {"type": "text", "content": "[1] ${option_1:Dashboard}"},
            {"type": "text", "content": "[2] ${option_2:Settings}"},
            {"type": "text", "content": "[3] ${option_3:Reports}"},
            {"type": "text", "content": "[4] ${option_4:Exit}"},
        ],
    },
}

# Write config files
(CONFIG_DIR / "app_header.json").write_text(json.dumps(app_header_config, indent=2))
(CONFIG_DIR / "dashboard.json").write_text(json.dumps(dashboard_config, indent=2))
(CONFIG_DIR / "alerts.json").write_text(json.dumps(alerts_config, indent=2))
(CONFIG_DIR / "menu.json").write_text(json.dumps(menu_config, indent=2))

# =============================================================================
# 1. Load and Render Simple Config
# =============================================================================

console.rule("[yellow]1. Load Simple Config[/]")
console.newline()

# Load header from JSON file
header = load_file(CONFIG_DIR / "app_header.json")
console.render_object(header)
console.newline()

# =============================================================================
# 2. Load Config with Variables
# =============================================================================

console.rule("[yellow]2. Config with Runtime Variables[/]")
console.newline()

# Load dashboard with runtime data
dashboard = load_file(
    CONFIG_DIR / "dashboard.json",
    variables={
        "cpu_usage": "45%",
        "memory_usage": "8.2 GB / 16 GB",
        "disk_usage": "234 GB / 500 GB",
        "status_message": "All systems operational",
        "status_effect": "ocean",
    },
)
console.render_object(dashboard)
console.newline()

# Same config, different data (simulating degraded state)
dashboard_degraded = load_file(
    CONFIG_DIR / "dashboard.json",
    variables={
        "cpu_usage": "92% [bold red]HIGH[/]",
        "memory_usage": "15.1 GB / 16 GB [bold red]CRITICAL[/]",
        "disk_usage": "478 GB / 500 GB",
        "status_message": "System under heavy load!",
        "status_effect": "fire",
    },
)
console.render_object(dashboard_degraded)
console.newline()

# =============================================================================
# 3. Alert Templates from Config
# =============================================================================

console.rule("[yellow]3. Alert Templates from Config[/]")
console.newline()

# Load alert templates
alerts_data = json.loads((CONFIG_DIR / "alerts.json").read_text())

# Use different alert types
for alert_type, message in [
    ("info", "Backup completed successfully at 10:45 AM"),
    ("warning", "Disk usage above 80% threshold"),
    ("critical", "Database connection lost!"),
]:
    template = alerts_data["templates"][alert_type]
    alert = load_dict(template, variables={"message": message})
    console.render_object(alert)
    console.newline()

# =============================================================================
# 4. Dynamic Menu from Config
# =============================================================================

console.rule("[yellow]4. Dynamic Menu from Config[/]")
console.newline()

# Default menu
menu = load_file(CONFIG_DIR / "menu.json")
console.render_object(menu)
console.newline()

# Customized menu for admin users
admin_menu = load_file(
    CONFIG_DIR / "menu.json",
    variables={
        "menu_title": "Admin Panel",
        "option_1": "User Management",
        "option_2": "System Config",
        "option_3": "Audit Logs",
        "option_4": "Logout",
    },
)
console.render_object(admin_menu)
console.newline()

# =============================================================================
# 5. Inline JSON Definition
# =============================================================================

console.rule("[yellow]5. Inline JSON Definition[/]")
console.newline()

# Sometimes you want to define UI inline as JSON-like dicts
# This is useful for quick prototyping or dynamic generation

inline_ui = {
    "column": [
        {"frame": "Panel A", "title": "Left", "effect": "ocean"},
        {"frame": "Panel B", "title": "Right", "effect": "fire"},
    ],
    "gap": 1,
}

console.render_dict(inline_ui)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    """
[bold cyan]JSON Config Benefits:[/]

- Separate UI structure from application code
- Non-programmers can customize layouts
- Easy A/B testing of different designs
- Theme switching without code changes
- Dynamic content via ${variables}
- Reusable template libraries
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=1,
)

# Cleanup note
console.newline()
console.text(f"[dim]Config files created in: {CONFIG_DIR}[/]")
