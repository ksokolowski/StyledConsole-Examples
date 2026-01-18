#!/usr/bin/env python3
"""Config-Driven Dashboard Example - v0.10.0 Declarative API.

Demonstrates building complete dashboards from configuration,
enabling customizable monitoring displays without code changes.

Usage:
    python 10_v010_api/config_dashboard.py
"""

from styledconsole import Console, Declarative, icons, load_dict

console = Console()

# =============================================================================
# Dashboard Configuration (could be loaded from file)
# =============================================================================

DASHBOARD_CONFIG = {
    "name": "Production Monitor",
    "refresh_interval": 30,
    "theme": "dark",
    "layout": {
        "type": "layout",
        "direction": "vertical",
        "gap": 1,
        "children": [
            # Header section
            {
                "id": "header",
                "banner": "${app_name}",
                "font": "small",
                "effect": "rainbow",
            },
            # Metrics row
            {
                "id": "metrics",
                "type": "layout",
                "direction": "vertical",
                "gap": 1,
                "children": [
                    {
                        "frame": "${metrics_content}",
                        "title": "Live Metrics",
                        "effect": "steel",
                    },
                ],
            },
            # Services grid
            {
                "id": "services",
                "frame": "${services_content}",
                "title": "Services",
                "effect": "${services_effect}",
            },
            # Alerts section
            {
                "id": "alerts",
                "frame": "${alerts_content}",
                "title": "Recent Alerts (${alert_count})",
                "effect": "${alerts_effect}",
            },
        ],
    },
}

# Widget templates
WIDGET_TEMPLATES = {
    "metric_card": {
        "type": "text",
        "content": "${icon} ${label}: ${value}",
    },
    "service_row": {
        "type": "text",
        "content": "${status_icon} ${name} - ${status} (${uptime})",
    },
    "alert_row": {
        "type": "text",
        "content": "[${time}] ${level}: ${message}",
    },
}

# =============================================================================
# Simulated Data Sources
# =============================================================================


def get_metrics():
    """Simulate fetching metrics from monitoring system."""
    return {
        "cpu": {"value": "45%", "status": "ok"},
        "memory": {"value": "8.2 GB", "status": "ok"},
        "requests": {"value": "1,234/s", "status": "ok"},
        "errors": {"value": "0.02%", "status": "ok"},
        "latency": {"value": "45ms", "status": "ok"},
    }


def get_services():
    """Simulate fetching service status."""
    return [
        {"name": "api-gateway", "status": "running", "uptime": "15d 4h"},
        {"name": "auth-service", "status": "running", "uptime": "15d 4h"},
        {"name": "user-service", "status": "running", "uptime": "12d 8h"},
        {"name": "payment-service", "status": "degraded", "uptime": "2h 15m"},
        {"name": "notification-service", "status": "running", "uptime": "8d 12h"},
    ]


def get_alerts():
    """Simulate fetching recent alerts."""
    return [
        {"time": "10:45", "level": "warn", "message": "High memory on payment-service"},
        {"time": "10:32", "level": "info", "message": "Deployment completed: api-v2.4.1"},
        {"time": "09:15", "level": "info", "message": "Auto-scaled to 5 instances"},
    ]


# =============================================================================
# Dashboard Renderer
# =============================================================================


def render_metrics(metrics: dict) -> str:
    """Render metrics as formatted content."""
    lines = []
    icons_map = {
        "cpu": icons.GEAR,
        "memory": icons.HIGH_VOLTAGE,
        "requests": icons.SATELLITE_ANTENNA,
        "errors": icons.WARNING,
        "latency": icons.STOPWATCH,
    }
    labels = {
        "cpu": "CPU Usage",
        "memory": "Memory",
        "requests": "Requests",
        "errors": "Error Rate",
        "latency": "Avg Latency",
    }

    for key, data in metrics.items():
        icon = icons_map.get(key, icons.GEAR)
        label = labels.get(key, key)
        value = data["value"]
        lines.append(f"{icon} {label}: {value}")

    return "\n".join(lines)


def render_services(services: list) -> tuple[str, str]:
    """Render services and determine effect based on status."""
    lines = []
    all_healthy = True

    for svc in services:
        if svc["status"] == "running":
            icon = icons.CHECK_MARK_BUTTON
            status_text = f"[green]{svc['status']}[/]"
        elif svc["status"] == "degraded":
            icon = icons.WARNING
            status_text = f"[yellow]{svc['status']}[/]"
            all_healthy = False
        else:
            icon = icons.CROSS_MARK
            status_text = f"[red]{svc['status']}[/]"
            all_healthy = False

        lines.append(f"{icon} {svc['name']}: {status_text} (uptime: {svc['uptime']})")

    effect = "ocean" if all_healthy else "sunset"
    return "\n".join(lines), effect


def render_alerts(alerts: list) -> tuple[str, str, int]:
    """Render alerts and determine effect based on severity."""
    lines = []
    has_warning = False

    for alert in alerts:
        if alert["level"] == "warn":
            level_text = f"[yellow]WARN[/]"
            has_warning = True
        elif alert["level"] == "error":
            level_text = f"[red]ERROR[/]"
            has_warning = True
        else:
            level_text = f"[dim]INFO[/]"

        lines.append(f"[dim]{alert['time']}[/] {level_text} {alert['message']}")

    effect = "sunset" if has_warning else "steel"
    return "\n".join(lines), effect, len(alerts)


# =============================================================================
# Main Dashboard
# =============================================================================

console.text("[bold cyan]Config-Driven Dashboard - v0.10.0 API[/]")
console.text("[dim]Complete dashboard from configuration[/]")
console.newline()

# Fetch data
metrics = get_metrics()
services = get_services()
alerts = get_alerts()

# Render components
metrics_content = render_metrics(metrics)
services_content, services_effect = render_services(services)
alerts_content, alerts_effect, alert_count = render_alerts(alerts)

# Build dashboard with variables
dashboard = load_dict(
    DASHBOARD_CONFIG["layout"],
    variables={
        "app_name": DASHBOARD_CONFIG["name"].upper().replace(" ", ""),
        "metrics_content": metrics_content,
        "services_content": services_content,
        "services_effect": services_effect,
        "alerts_content": alerts_content,
        "alerts_effect": alerts_effect,
        "alert_count": str(alert_count),
    },
)

console.render_object(dashboard)
console.newline()

# =============================================================================
# Show Config Customization
# =============================================================================

console.rule("[yellow]Customization Demo[/]")
console.newline()

# Same config, different theme/data
CUSTOM_CONFIG = {
    "type": "layout",
    "direction": "vertical",
    "gap": 1,
    "children": [
        {"banner": "${title}", "font": "small", "effect": "${header_effect}"},
        {
            "frame": "${content}",
            "title": "${panel_title}",
            "effect": "${panel_effect}",
            "border": "${border_style}",
        },
    ],
}

# Render with "success" theme
success_dashboard = load_dict(
    CUSTOM_CONFIG,
    variables={
        "title": "SUCCESS",
        "header_effect": "ocean",
        "content": f"{icons.CHECK_MARK_BUTTON} All deployments successful\n{icons.CHECK_MARK_BUTTON} Tests passing\n{icons.CHECK_MARK_BUTTON} No alerts",
        "panel_title": "Deployment Status",
        "panel_effect": "ocean",
        "border_style": "rounded",
    },
)
console.render_object(success_dashboard)
console.newline()

# Render with "error" theme
error_dashboard = load_dict(
    CUSTOM_CONFIG,
    variables={
        "title": "ALERT",
        "header_effect": "fire",
        "content": f"{icons.CROSS_MARK} Deployment failed\n{icons.WARNING} 3 tests failing\n{icons.CROSS_MARK} Database unreachable",
        "panel_title": "Critical Issues",
        "panel_effect": "fire",
        "border_style": "double",
    },
)
console.render_object(error_dashboard)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
[bold cyan]Config-Driven Dashboard Benefits:[/]

{icons.SPARKLES} Single config defines entire dashboard layout
{icons.SPARKLES} Swap themes/effects via variables
{icons.SPARKLES} Dynamic content from any data source
{icons.SPARKLES} Reusable widget templates
{icons.SPARKLES} Easy to version control and deploy
{icons.SPARKLES} Non-developers can modify appearance
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=1,
)
