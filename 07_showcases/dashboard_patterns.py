#!/usr/bin/env python3
"""Quick Reference - Dashboard Patterns with Frames and Columns.

Shows the most common patterns for combining frames with columns
to create structured dashboard layouts.

Usage:
    python 07_showcases/dashboard_patterns.py
"""

from styledconsole import Console, icons

console = Console()

console.text("[bold cyan]Dashboard Design Patterns[/]")
console.text("[dim]Combining frames and columns for structured layouts[/]")
console.newline()

# =============================================================================
# Pattern 1: Frame with Aligned Metrics
# =============================================================================

console.rule("[yellow]Pattern 1: Frame with Aligned Metrics[/]")
console.newline()

console.frame(
    """
CPU:  45%    Memory: 12GB    Disk: 32%    Network: ↑125MB/s
    """.strip(),
    title="System Overview",
    border="rounded",
    border_color="cyan",
)
console.newline()

# =============================================================================
# Pattern 2: Columns for Side-by-Side Data
# =============================================================================

console.rule("[yellow]Pattern 2: Columns for Side-by-Side Data[/]")
console.newline()

console.columns(
    [
        f"{icons.CHECK_MARK_BUTTON} Service A\nStatus: Running\nUptime: 99.9%",
        f"{icons.WARNING} Service B\nStatus: Degraded\nUptime: 95.2%",
        f"{icons.CROSS_MARK} Service C\nStatus: Down\nUptime: 0%",
    ],
    padding=(0, 3),
    equal=True,
)
console.newline()

# =============================================================================
# Pattern 3: Frame Group with Vertical Sections
# =============================================================================

console.rule("[yellow]Pattern 3: Frame Group with Vertical Sections[/]")
console.newline()

console.frame_group(
    [
        {
            "content": "Requests:  45.2K\nSuccess:   44.8K\nFailed:    400",
            "title": "Traffic",
            "border": "rounded",
            "border_color": "green",
        },
        {
            "content": "4xx: 350\n5xx: 50\nTimeout: 25",
            "title": "Errors",
            "border": "rounded",
            "border_color": "red",
        },
    ],
    gap=1,
)
console.newline()

# =============================================================================
# Pattern 4: Tabular Data with Columns
# =============================================================================

console.rule("[yellow]Pattern 4: Tabular Data with Columns[/]")
console.newline()

console.columns(
    [
        "[bold]Metric[/]\nLatency\nThroughput\nErrors",
        "[bold]Value[/]\n125ms\n450/s\n0.8%",
        "[bold]Status[/]\n[green]Good[/]\n[green]Good[/]\n[yellow]OK[/]",
    ],
    padding=(0, 4),
    equal=True,
)
console.newline()

# =============================================================================
# Pattern 5: Nested - Outer Frame with Inner Columns
# =============================================================================

console.rule("[yellow]Pattern 5: Nested - Outer Frame with Inner Columns[/]")
console.newline()

console.frame(
    f"""
[bold]Recent Deployments:[/]

{icons.CHECK_MARK_BUTTON} v2.4.1       Production     10:45:23
{icons.WARNING} v2.5.0-rc    Staging        10:30:15
{icons.GEAR} v2.6.0-dev   Development    10:15:08
    """.strip(),
    title="Deployment History",
    border="double",
    border_color="dodgerblue",
    padding=1,
)
console.newline()

# =============================================================================
# Pattern 6: Multi-Section Dashboard
# =============================================================================

console.rule("[yellow]Pattern 6: Multi-Section Dashboard[/]")
console.newline()

# Header with key metrics
console.frame(
    """
Active Users: 1,234    Requests/min: 850    Errors: 12    Avg Response: 125ms
    """.strip(),
    title="Live Metrics",
    border="heavy",
    border_gradient_start="cyan",
    border_gradient_end="blue",
)
console.newline()

# Service status in columns
console.text("[bold]Service Status:[/]")
console.columns(
    [
        f"{icons.CHECK_MARK_BUTTON} Web",
        f"{icons.CHECK_MARK_BUTTON} API",
        f"{icons.CHECK_MARK_BUTTON} DB",
        f"{icons.CROSS_MARK} Cache",
    ],
    padding=(0, 3),
)
console.newline()

# Activity log
console.frame(
    """
10:45    Deployment completed successfully
10:42    High memory alert - investigated
10:38    Backup job finished
    """.strip(),
    title="Recent Activity",
    border="minimal",
    border_color="yellow",
)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
[bold cyan]Key Takeaways:[/]

{icons.SPARKLES} Use [bold]frame()[/] for boxed content with titles
{icons.SPARKLES} Use [bold]columns()[/] for side-by-side alignment
{icons.SPARKLES} Use [bold]frame_group()[/] for vertical stacking with outer frame
{icons.SPARKLES} Combine patterns for complex dashboards
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=2,
)
