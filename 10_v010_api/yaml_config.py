#!/usr/bin/env python3
"""YAML Configuration Example - v0.10.0 Declarative API.

Demonstrates loading UI definitions from YAML files - a more
human-readable format for complex configurations.

YAML advantages over JSON:
- Comments support
- Multiline strings
- No trailing commas issues
- More compact syntax
- Anchors and aliases for reuse

Requirements:
    pip install styledconsole[yaml]
    # or: pip install pyyaml

Usage:
    python 10_v010_api/yaml_config.py
"""

from pathlib import Path

from styledconsole import Console, icons, load_file, load_yaml

console = Console()

console.text("[bold cyan]YAML Configuration Demo - v0.10.0 API[/]")
console.text("[dim]Human-readable UI definitions with YAML[/]")
console.newline()

# =============================================================================
# Create sample YAML files
# =============================================================================

CONFIG_DIR = Path(__file__).parent / "configs"
CONFIG_DIR.mkdir(exist_ok=True)

# Dashboard YAML - showcasing YAML features
dashboard_yaml = """\
# Dashboard Configuration
# This YAML file defines a complete monitoring dashboard

# Reusable effect definitions (YAML anchors)
effects:
  healthy: &healthy_effect ocean
  warning: &warning_effect sunset
  critical: &critical_effect fire

# Main layout
type: layout
direction: vertical
gap: 1
children:
  # Header banner
  - banner: MONITOR
    font: small
    effect: rainbow

  # System metrics panel
  - frame: |
      CPU:     ${cpu}
      Memory:  ${memory}
      Disk:    ${disk}
      Network: ${network}
    title: System Metrics
    effect: ${metrics_effect}
    border: rounded

  # Service status
  - frame: ${services}
    title: "Services (${service_count} total)"
    effect: ${services_effect}

  # Recent events
  - frame: ${events}
    title: Recent Events
    effect: steel
    border: minimal
"""

# Theme configuration YAML
theme_yaml = """\
# Theme Configuration
# Define reusable themes for your application

themes:
  light:
    primary_effect: ocean
    secondary_effect: steel
    warning_effect: sunset
    error_effect: fire
    border_style: rounded

  dark:
    primary_effect: aurora
    secondary_effect: steel
    warning_effect: fire
    error_effect: fire
    border_style: heavy

  cyberpunk:
    primary_effect: neon
    secondary_effect: rainbow
    warning_effect: fire
    error_effect: fire
    border_style: double
"""

# Application layout YAML
app_layout_yaml = """\
# Application Layout
# Main application structure with header, content, and footer

type: layout
direction: vertical
gap: 1
children:
  # Header
  - type: layout
    direction: vertical
    gap: 0
    children:
      - banner: ${app_name}
        font: small
        effect: ${header_effect}
      - frame: "${tagline}"
        effect: ${accent_effect}
        border: rounded

  # Main content area
  - frame: |
      ${main_content}
    title: "${content_title}"
    effect: ${content_effect}
    border: "${border_style}"

  # Footer
  - type: text
    content: "${footer_text}"
"""

# Alerts configuration YAML
alerts_yaml = """\
# Alert Templates
# Predefined alert styles for different severity levels

templates:
  info:
    frame: "${message}"
    title: "Info"
    effect: ocean
    border: rounded

  success:
    frame: "${message}"
    title: "Success"
    effect: ocean
    border: rounded

  warning:
    frame: "${message}"
    title: "Warning"
    effect: sunset
    border: heavy

  error:
    frame: "${message}"
    title: "Error"
    effect: fire
    border: double

  critical:
    frame: |
      CRITICAL ALERT

      ${message}

      Time: ${timestamp}
      Source: ${source}
    title: "CRITICAL"
    effect: fire
    border: double
"""

# Write YAML files
(CONFIG_DIR / "dashboard.yaml").write_text(dashboard_yaml)
(CONFIG_DIR / "themes.yaml").write_text(theme_yaml)
(CONFIG_DIR / "app_layout.yaml").write_text(app_layout_yaml)
(CONFIG_DIR / "alerts.yaml").write_text(alerts_yaml)

# =============================================================================
# 1. Load Dashboard from YAML
# =============================================================================

console.rule("[yellow]1. Dashboard from YAML[/]")
console.newline()

# Simulate metrics data
services_list = [
    f"{icons.CHECK_MARK_BUTTON} api-gateway: running",
    f"{icons.CHECK_MARK_BUTTON} database: running",
    f"{icons.WARNING} cache: degraded",
]

events_list = [
    "[dim]10:45[/] Deployment completed",
    "[dim]10:30[/] Auto-scaling triggered",
    "[dim]10:15[/] Backup finished",
]

dashboard = load_file(
    CONFIG_DIR / "dashboard.yaml",
    variables={
        "cpu": "45%",
        "memory": "8.2 GB / 16 GB",
        "disk": "234 GB / 500 GB",
        "network": "↑ 125 MB/s  ↓ 89 MB/s",
        "metrics_effect": "steel",
        "services": "\n".join(services_list),
        "service_count": "3",
        "services_effect": "sunset",
        "events": "\n".join(events_list),
    },
)
console.render_object(dashboard)
console.newline()

# =============================================================================
# 2. Application Layout from YAML
# =============================================================================

console.rule("[yellow]2. Application Layout from YAML[/]")
console.newline()

app = load_file(
    CONFIG_DIR / "app_layout.yaml",
    variables={
        "app_name": "MYAPP",
        "tagline": "Your productivity companion",
        "header_effect": "rainbow",
        "accent_effect": "ocean",
        "content_title": "Dashboard",
        "main_content": f"{icons.CHART_INCREASING} Sales: $45,230\n{icons.BUSTS_IN_SILHOUETTE} Users: 1,234\n{icons.SPARKLES} Growth: +12%",
        "content_effect": "steel",
        "border_style": "rounded",
        "footer_text": "[dim]v2.0.0 | Last updated: 10:45 AM[/]",
    },
)
console.render_object(app)
console.newline()

# =============================================================================
# 3. Alert Templates from YAML
# =============================================================================

console.rule("[yellow]3. Alert Templates from YAML[/]")
console.newline()

import yaml

alerts_data = yaml.safe_load((CONFIG_DIR / "alerts.yaml").read_text())

# Show different alert types
for alert_type, message in [
    ("info", "System backup scheduled for 2:00 AM"),
    ("warning", "Memory usage above 80%"),
    ("error", "Failed to connect to external API"),
]:
    template = alerts_data["templates"][alert_type]
    alert = load_yaml(
        yaml.dump(template),
        variables={"message": message},
    )
    console.render_object(alert)
    console.newline()

# Critical alert with more details
critical_template = alerts_data["templates"]["critical"]
critical_alert = load_yaml(
    yaml.dump(critical_template),
    variables={
        "message": "Database connection pool exhausted!",
        "timestamp": "2024-01-15 10:45:23",
        "source": "db-primary-01",
    },
)
console.render_object(critical_alert)
console.newline()

# =============================================================================
# 4. Inline YAML Definition
# =============================================================================

console.rule("[yellow]4. Inline YAML Definition[/]")
console.newline()

# Define UI inline as YAML string
inline_yaml = """\
type: layout
direction: vertical
gap: 1
children:
  - frame: |
      This is a multiline
      content block defined
      directly in YAML
    title: Inline YAML
    effect: ocean

  - frame: Single line content
    title: Simple Frame
    effect: steel
"""

inline_ui = load_yaml(inline_yaml)
console.render_object(inline_ui)
console.newline()

# =============================================================================
# 5. YAML vs JSON Comparison
# =============================================================================

console.rule("[yellow]5. YAML vs JSON Comparison[/]")
console.newline()

comparison_yaml = """\
# YAML is more readable:
# - Supports comments (like this one!)
# - No quotes needed for simple strings
# - Multiline strings with |
# - No commas or brackets clutter

type: frame
title: YAML Benefits
effect: ocean
border: rounded
content: |
  Comments:     Supported in YAML
  Quotes:       Optional for strings
  Multiline:    Easy with | or >
  Readability:  Much cleaner
"""

comparison = load_yaml(comparison_yaml)
console.render_object(comparison)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
[bold cyan]YAML Configuration Benefits:[/]

{icons.SPARKLES} Comments for documentation
{icons.SPARKLES} Multiline strings with | or >
{icons.SPARKLES} No trailing comma issues
{icons.SPARKLES} More readable than JSON
{icons.SPARKLES} Anchors & aliases for reuse
{icons.SPARKLES} Perfect for config files

[bold]Install:[/] pip install styledconsole[yaml]
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=1,
)

console.newline()
console.text(f"[dim]YAML files created in: {CONFIG_DIR}[/]")
