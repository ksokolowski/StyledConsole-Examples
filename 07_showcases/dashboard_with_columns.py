#!/usr/bin/env python3
"""Dashboard with Columns - Combining frames and columns for structured layouts.

Demonstrates how to use StyledColumns alongside frames to create
professional dashboards with aligned content and clean spacing.

Usage:
    python 07_showcases/dashboard_with_columns.py
"""

from styledconsole import Console, EffectSpec, icons

console = Console()

console.banner("DASHBOARD", font="small", effect=EffectSpec.gradient("cyan", "blue"))
console.newline()

# =============================================================================
# System Status Dashboard
# =============================================================================

console.rule("System Status Dashboard")
console.newline()

# Frame with column-formatted content inside
console.frame(
    f"""
[bold]CPU Cores:[/]
{icons.CHECK_MARK_BUTTON} Core 1: 45%    {icons.CHECK_MARK_BUTTON} Core 2: 38%    {icons.WARNING} Core 3: 82%    {icons.CHECK_MARK_BUTTON} Core 4: 51%

[bold]Memory:[/]
Total: 16 GB      Used: 12 GB      Free: 4 GB      Cache: 2 GB

[bold]Disk Usage:[/]
{icons.CHECK_MARK_BUTTON} /dev/sda1: 45%         {icons.WARNING} /dev/sda2: 78%         {icons.CHECK_MARK_BUTTON} /dev/sdb1: 32%
    """.strip(),
    title="System Resources",
    border="double",
    border_gradient_start="cyan",
    border_gradient_end="blue",
    padding=2,
)
console.newline()

# =============================================================================
# StyledColumns with Frames Side-by-Side
# =============================================================================

console.rule("Services Status (Using Columns)")
console.newline()

# Use columns to display multiple frames side-by-side
console.text("[bold cyan]Using console.columns() for side-by-side frames:[/]")
console.newline()

# Services column
console.columns(
    [
        f"{icons.CHECK_MARK_BUTTON} Web Server\n{icons.CHECK_MARK_BUTTON} Database\n{icons.CROSS_MARK} Cache\n{icons.WARNING} API Gateway",
        f"Total: 45.2K\nSuccess: 44.8K\nFailed: 400\nAvg: 125ms",
        f"4xx: 350\n5xx: 50\nTimeout: 25\nNetwork: 15",
    ],
    padding=(0, 3),
    equal=True,
)
console.newline()

# =============================================================================
# Application Status  
# =============================================================================

console.rule("Application Monitoring")
console.newline()

console.frame_group(
    [
        {
            "content": f"""
{icons.CHECK_MARK_BUTTON} Web Server       Running
{icons.CHECK_MARK_BUTTON} Database         Running  
{icons.CROSS_MARK} Cache            Stopped
{icons.WARNING} API Gateway      Degraded
            """.strip(),
            "title": "Services",
            "border": "rounded",
            "border_color": "green",
        },
        {
            "content": """
Total:    45.2K
Success:  44.8K
Failed:   400
Avg Time: 125ms
            """.strip(),
            "title": "Requests (Last Hour)",
            "border": "rounded",
            "border_color": "dodgerblue",
        },
        {
            "content": """
4xx Errors:  350
5xx Errors:  50  
Timeouts:    25
Network:     15
            """.strip(),
            "title": "Error Breakdown",
            "border": "rounded",
            "border_color": "red",
        },
    ],
    title="Application Health",
    border="double",
    border_gradient_start="green",
    border_gradient_end="red",
    gap=1,
)
console.newline()

# =============================================================================
# Deployment Status with Columns
# =============================================================================

console.rule("Deployment Status")
console.newline()

# Environments displayed in columns
console.text("[bold cyan]Environment Status:[/]")
console.newline()

console.columns(
    [
        f"{icons.CHECK_MARK_BUTTON} Production\nv2.4.1\n[green]Healthy[/green]",
        f"{icons.WARNING} Staging\nv2.5.0-rc1\n[yellow]Testing[/yellow]",
        f"{icons.GEAR} Development\nv2.6.0-dev\n[cyan]Building[/cyan]",
    ],
    padding=(0, 4),
    equal=True,
    align="center",
)
console.newline()

# =============================================================================
# Activity Log with Aligned Columns
# =============================================================================

console.rule("Activity Log")
console.newline()

# Log entries with timestamp + message in columns - properly aligned!
console.text("[bold yellow]Recent Events:[/]")
console.newline()

console.columns(
    [
        "10:45:23\n10:42:15\n10:38:09\n10:35:44\n10:32:18",
        f"{icons.CHECK_MARK_BUTTON} Deployment successful\n{icons.WARNING} High memory usage detected\n{icons.CHECK_MARK_BUTTON} Backup completed\n{icons.GEAR} Starting maintenance window\n{icons.CHECK_MARK_BUTTON} Health check passed",
    ],
    padding=(0, 3),
)
console.newline()

# =============================================================================
# Multi-Column Metrics Table
# =============================================================================

console.rule("Performance Metrics")
console.newline()

# Using columns for tabular data
console.text("[bold cyan]Last 24 Hours:[/]")
console.newline()

console.columns(
    [
        "[bold]Metric[/]\nResponse Time\nThroughput\nError Rate",
        "[bold]Current[/]\n125ms\n450 req/s\n0.8%",
        "[bold]Change[/]\n[green]↓ 12%[/green]\n[green]↑ 8%[/green]\n[green]↓ 0.2%[/green]",
    ],
    padding=(0, 4),
    equal=True,
    align="center",
)
console.newline()

# =============================================================================
# Team Status Grid
# =============================================================================

console.rule("Team Status")
console.newline()

console.frame(
    """
[bold]Member          Role         Status[/]
{check} Alice        Backend      [green]Available[/]
{check} Bob          Frontend     [green]Available[/]
{warn} Charlie      DevOps       [yellow]In Meeting[/]
{cross} David        Database     [red]Offline[/]
    """.format(
        check=icons.CHECK_MARK_BUTTON,
        warn=icons.WARNING,
        cross=icons.CROSS_MARK,
    ).strip(),
    title="Team Availability",
    border="rounded",
    border_color="dodgerblue",
    padding=1,
)
console.newline()

# =============================================================================
# File Browser with Columns
# =============================================================================

console.rule("File Browser")
console.newline()

# Files displayed in columns with metadata
console.columns(
    [
        f"{icons.BOOKMARK} config.json\n{icons.BOOKMARK} main.py\n{icons.BOOKMARK} README.md\n{icons.BOOKMARK} test.py",
        "2.4 KB\n15.8 KB\n3.1 KB\n8.2 KB",
        "2025-01-06\n2025-01-06\n2025-01-05\n2025-01-06",
    ],
    padding=(0, 4),
)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
{icons.SPARKLES} Aligned Content: Columns provide perfect alignment for dashboard data
{icons.SPARKLES} Side-by-Side: Use columns() to display frames horizontally
{icons.SPARKLES} Clean Spacing: Control padding and gaps for professional look
{icons.SPARKLES} Tabular Data: Columns work great for metrics and status displays
    """.strip(),
    title="Dashboard Design with Columns",
    border="rounded_thick",
    border_color="lime",
)
