#!/usr/bin/env python3
"""Jinja2 Templates Example - v0.10.0 Declarative API.

Demonstrates powerful templating with Jinja2 for:
- Loops and iteration
- Conditionals
- Filters
- Template inheritance
- Dynamic UI generation

Requirements:
    pip install styledconsole[jinja]

Usage:
    python 10_v010_api/jinja_templates.py
"""

from pathlib import Path

from styledconsole import (
    Console,
    add_jinja_filter,
    icons,
    load_jinja_file,
    render_jinja,
)

console = Console()

console.text("[bold cyan]Jinja2 Templates Demo - v0.10.0 API[/]")
console.text("[dim]Powerful templating with loops, conditionals, and filters[/]")
console.newline()

# =============================================================================
# 1. Basic Jinja2 Template with Conditionals
# =============================================================================

console.rule("[yellow]1. Conditionals[/]")
console.newline()

status_template = """\
type: frame
title: "{{ title }}"
content: "{{ message }}"
effect: "{{ 'ocean' if success else 'fire' }}"
border: "{{ 'rounded' if success else 'double' }}"
"""

# Render success state
success_ui = render_jinja(
    status_template,
    title="Operation Result",
    message=f"{icons.CHECK_MARK_BUTTON} All tasks completed successfully",
    success=True,
)
console.render_object(success_ui)
console.newline()

# Render failure state
failure_ui = render_jinja(
    status_template,
    title="Operation Result",
    message=f"{icons.CROSS_MARK} Failed to complete tasks",
    success=False,
)
console.render_object(failure_ui)
console.newline()

# =============================================================================
# 2. Loops - Generate UI from Collections
# =============================================================================

console.rule("[yellow]2. Loops - Dynamic Lists[/]")
console.newline()

# Services data
services = [
    {"name": "api-gateway", "status": "running", "cpu": 23, "memory": 512},
    {"name": "database", "status": "running", "cpu": 45, "memory": 2048},
    {"name": "cache", "status": "degraded", "cpu": 78, "memory": 1024},
    {"name": "worker", "status": "stopped", "cpu": 0, "memory": 0},
]

services_template = """\
type: frame
title: "Services ({{ services | length }} total)"
effect: steel
content:
  type: layout
  direction: vertical
  children:
    {% for svc in services %}
    - type: text
      content: "{{ svc.status | status_icon }} {{ svc.name }}: {{ svc.status }} (CPU: {{ svc.cpu }}%, Mem: {{ svc.memory }}MB)"
    {% endfor %}
"""

services_ui = render_jinja(services_template, services=services)
console.render_object(services_ui)
console.newline()

# =============================================================================
# 3. Built-in Filters
# =============================================================================

console.rule("[yellow]3. Built-in Filters[/]")
console.newline()

filters_template = """\
type: layout
direction: vertical
gap: 1
children:
  # Status icon filter
  - type: frame
    title: "status_icon filter"
    effect: steel
    content: |
      running  → {{ "running" | status_icon }}
      warning  → {{ "warning" | status_icon }}
      error    → {{ "error" | status_icon }}
      stopped  → {{ "stopped" | status_icon }}

  # Status effect filter
  - type: frame
    title: "status_effect filter"
    effect: steel
    content: |
      running → {{ "running" | status_effect }}
      warning → {{ "warning" | status_effect }}
      error   → {{ "error" | status_effect }}

  # Icon filter
  - type: frame
    title: "icon filter"
    effect: steel
    content: |
      check    → {{ "check" | icon }}
      star     → {{ "star" | icon }}
      rocket   → {{ "rocket" | icon }}
      fire     → {{ "fire" | icon }}
"""

filters_ui = render_jinja(filters_template)
console.render_object(filters_ui)
console.newline()

# =============================================================================
# 4. Complex Dashboard with Loops and Conditionals
# =============================================================================

console.rule("[yellow]4. Complex Dashboard[/]")
console.newline()

dashboard_data = {
    "title": "MONITOR",
    "metrics": [
        {"name": "CPU", "value": 45, "unit": "%", "threshold": 80},
        {"name": "Memory", "value": 8.2, "unit": "GB", "threshold": 14},
        {"name": "Disk", "value": 234, "unit": "GB", "threshold": 400},
        {"name": "Network", "value": 125, "unit": "MB/s", "threshold": 1000},
    ],
    "alerts": [
        {"level": "warning", "message": "High memory usage on node-3"},
        {"level": "info", "message": "Backup completed successfully"},
        {"level": "info", "message": "Auto-scaling triggered"},
    ],
}

dashboard_template = """\
type: layout
direction: vertical
gap: 1
children:
  # Header
  - banner: "{{ title }}"
    font: small
    effect: rainbow

  # Metrics panel
  - type: frame
    title: "System Metrics"
    effect: steel
    content:
      type: layout
      direction: vertical
      children:
        {% for m in metrics %}
        {% set status = 'warning' if m.value > m.threshold * 0.8 else 'ok' %}
        - type: text
          content: "{{ status | status_icon }} {{ m.name }}: {{ m.value }}{{ m.unit }}{% if m.value > m.threshold * 0.8 %} [yellow](High)[/]{% endif %}"
        {% endfor %}

  # Alerts panel
  - type: frame
    title: "Recent Alerts ({{ alerts | length }})"
    effect: "{{ 'sunset' if alerts | selectattr('level', 'eq', 'warning') | list else 'steel' }}"
    content:
      type: layout
      direction: vertical
      children:
        {% for alert in alerts %}
        - type: text
          content: "{% if alert.level == 'warning' %}{{ 'warning' | status_icon }}{% else %}{{ 'info' | icon }}{% endif %} {{ alert.message }}"
        {% endfor %}
"""

dashboard_ui = render_jinja(dashboard_template, **dashboard_data)
console.render_object(dashboard_ui)
console.newline()

# =============================================================================
# 5. Custom Filters
# =============================================================================

console.rule("[yellow]5. Custom Filters[/]")
console.newline()


# Register custom filters
def format_bytes(value: int) -> str:
    """Format bytes to human readable."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if abs(value) < 1024:
            return f"{value:.1f} {unit}"
        value /= 1024  # type: ignore
    return f"{value:.1f} PB"


def progress_bar(value: int, max_value: int = 100, width: int = 20) -> str:
    """Create a text progress bar."""
    filled = int(width * value / max_value)
    empty = width - filled
    return f"[{'█' * filled}{'░' * empty}] {value}%"


add_jinja_filter("bytes", format_bytes)
add_jinja_filter("progress", progress_bar)

custom_filters_template = """\
type: frame
title: "Custom Filters Demo"
effect: ocean
content: |
  File sizes (bytes filter):
    1024      → {{ 1024 | bytes }}
    1048576   → {{ 1048576 | bytes }}
    1073741824 → {{ 1073741824 | bytes }}

  Progress bars (progress filter):
    25%  {{ 25 | progress }}
    50%  {{ 50 | progress }}
    75%  {{ 75 | progress }}
    100% {{ 100 | progress }}
"""

custom_ui = render_jinja(custom_filters_template)
console.render_object(custom_ui)
console.newline()

# =============================================================================
# 6. Load from Jinja2 File
# =============================================================================

console.rule("[yellow]6. Load from .j2 File[/]")
console.newline()

# Create a sample .j2 file
CONFIG_DIR = Path(__file__).parent / "configs"
CONFIG_DIR.mkdir(exist_ok=True)

j2_template = """\
# Server Status Dashboard
# This template generates a status panel for multiple servers

type: layout
direction: vertical
gap: 1
children:
  - type: frame
    title: "Server Fleet ({{ servers | length }} servers)"
    effect: "{{ 'ocean' if all_healthy else 'sunset' }}"
    content:
      type: layout
      direction: vertical
      children:
        {% for server in servers %}
        - type: text
          content: "{{ server.status | status_icon }} {{ server.name }} - {{ server.ip }} ({{ server.region }})"
        {% endfor %}

  - type: frame
    title: "Summary"
    effect: steel
    content: |
      Total: {{ servers | length }}
      Healthy: {{ servers | selectattr('status', 'eq', 'running') | list | length }}
      Degraded: {{ servers | selectattr('status', 'eq', 'degraded') | list | length }}
      Down: {{ servers | selectattr('status', 'eq', 'stopped') | list | length }}
"""

(CONFIG_DIR / "servers.yaml.j2").write_text(j2_template)

# Load and render
servers_data = {
    "servers": [
        {"name": "web-01", "ip": "10.0.1.1", "region": "us-east", "status": "running"},
        {"name": "web-02", "ip": "10.0.1.2", "region": "us-east", "status": "running"},
        {"name": "api-01", "ip": "10.0.2.1", "region": "us-west", "status": "degraded"},
        {"name": "db-01", "ip": "10.0.3.1", "region": "eu-west", "status": "running"},
    ],
    "all_healthy": False,  # One server is degraded
}

servers_ui = load_jinja_file(CONFIG_DIR / "servers.yaml.j2", **servers_data)
console.render_object(servers_ui)
console.newline()

# =============================================================================
# 7. Table Generation with Loops
# =============================================================================

console.rule("[yellow]7. Table Generation[/]")
console.newline()

table_template = """\
type: frame
title: "{{ title }}"
effect: steel
border: rounded
content: |
  {% for row in rows %}
  {% if loop.first %}
  {{ "%-15s" | format(columns[0]) }} {{ "%-10s" | format(columns[1]) }} {{ "%-10s" | format(columns[2]) }}
  {{ "-" * 40 }}
  {% endif %}
  {{ "%-15s" | format(row[0]) }} {{ "%-10s" | format(row[1]) }} {{ "%-10s" | format(row[2]) }}
  {% endfor %}
"""

table_ui = render_jinja(
    table_template,
    title="User Activity",
    columns=["User", "Actions", "Status"],
    rows=[
        ["alice", "42", "active"],
        ["bob", "18", "active"],
        ["charlie", "7", "idle"],
        ["diana", "0", "offline"],
    ],
)
console.render_object(table_ui)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
[bold cyan]Jinja2 Template Benefits:[/]

{icons.SPARKLES} Loops with {{% for item in items %}}
{icons.SPARKLES} Conditionals with {{% if condition %}}
{icons.SPARKLES} Built-in filters: status_icon, status_effect, icon
{icons.SPARKLES} Custom filters via add_jinja_filter()
{icons.SPARKLES} Load from .yaml.j2 or .json.j2 files
{icons.SPARKLES} Full Jinja2 power: macros, inheritance, etc.

[bold]Install:[/] pip install styledconsole[jinja]
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=1,
)

console.newline()
console.text(f"[dim]Template files created in: {CONFIG_DIR}[/]")
