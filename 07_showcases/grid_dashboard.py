#!/usr/bin/env python3
"""Grid-Based Dashboard Layouts.

Demonstrates complex dashboard compositions using:
- frame_group() with grid layout
- Multiple columns and rows
- Mixed frame sizes
- Real-time monitoring patterns
- Background effects on dashboard cards

This is a more advanced example showing how to build
production-quality monitoring dashboards.
"""

from styledconsole import Console, EffectSpec, RenderPolicy, icons
from styledconsole.enums import Border, Effect, LayoutMode

# Use color-enabled policy
console = Console(policy=RenderPolicy(color=True, unicode=True, emoji=True))

# =============================================================================
# 1. Simple 2x2 Metric Grid
# =============================================================================

console.frame(
    "Grid Dashboard Layouts",
    title="Dashboard Demo",
    effect=Effect.RAINBOW,
)
console.newline()

console.rule("[cyan]1. Simple 2x2 Metric Grid[/]")
console.newline()

# Basic metrics grid
metrics_2x2 = [
    {"title": "Requests/sec", "content": "12,847", "effect": Effect.SUCCESS},
    {"title": "Avg Latency", "content": "42ms", "effect": Effect.INFO},
    {"title": "Error Rate", "content": "0.02%", "effect": Effect.SUCCESS},
    {"title": "Active Users", "content": "3,291", "effect": Effect.OCEAN},
]

console.frame_group(
    metrics_2x2,
    layout=LayoutMode.GRID,
    columns=2,
    item_width=30,
    border=Border.ROUNDED,
)
console.newline()

# =============================================================================
# 2. 3-Column Status Grid
# =============================================================================

console.rule("[cyan]2. 3-Column Service Status Grid[/]")
console.newline()

services = [
    {"title": "API", "content": f"{icons.CHECK_MARK_BUTTON} Online", "effect": Effect.SUCCESS},
    {"title": "Auth", "content": f"{icons.CHECK_MARK_BUTTON} Online", "effect": Effect.SUCCESS},
    {"title": "Database", "content": f"{icons.CHECK_MARK_BUTTON} Online", "effect": Effect.SUCCESS},
    {"title": "Cache", "content": f"{icons.WARNING} Degraded", "effect": Effect.WARNING},
    {"title": "Queue", "content": f"{icons.CHECK_MARK_BUTTON} Online", "effect": Effect.SUCCESS},
    {"title": "Search", "content": f"{icons.CROSS_MARK} Offline", "effect": Effect.ERROR},
]

console.frame_group(
    services,
    layout=LayoutMode.GRID,
    columns=3,
    item_width=22,
    border=Border.ROUNDED,
)
console.newline()

# =============================================================================
# 3. Dashboard with Header and Grid
# =============================================================================

console.rule("[cyan]3. Complete Dashboard Layout[/]")
console.newline()

# Header banner
console.banner("MONITOR", font="small", effect=Effect.OCEAN)
console.newline()

# Status bar
console.frame(
    f"{icons.GLOBE_WITH_MERIDIANS} Region: us-east-1  |  "
    f"{icons.ALARM_CLOCK} Updated: 14:32:15  |  "
    f"{icons.CHECK_MARK_BUTTON} All Systems Operational",
    effect=Effect.INFO,
    border=Border.MINIMAL,
)
console.newline()

# Main metrics grid
console.text("[bold]Performance Metrics[/]")
perf_metrics = [
    {"title": "CPU Usage", "content": "45%\n████████░░░░░░░░", "effect": Effect.SUCCESS},
    {"title": "Memory", "content": "72%\n████████████░░░░", "effect": Effect.WARNING},
    {"title": "Disk I/O", "content": "23%\n████░░░░░░░░░░░░", "effect": Effect.SUCCESS},
    {"title": "Network", "content": "1.2 GB/s\n██████████░░░░░░", "effect": Effect.INFO},
]

console.frame_group(
    perf_metrics,
    layout=LayoutMode.GRID,
    columns=2,
    item_width=35,
    border=Border.DOUBLE,
)
console.newline()

# =============================================================================
# 4. Grid with Background Gradients
# =============================================================================

console.rule("[cyan]4. Grid with Background Gradients[/]")
console.newline()

# Cards with individual background effects
bg_cards = [
    {
        "title": "Revenue",
        "content": "$142,847\n+12.5% MTD",
        "effect": EffectSpec.gradient("#10b981", "#059669", layer="background"),
    },
    {
        "title": "Orders",
        "content": "8,291\n+8.2% MTD",
        "effect": EffectSpec.gradient("#3b82f6", "#2563eb", layer="background"),
    },
    {
        "title": "Customers",
        "content": "2,847\n+15.3% MTD",
        "effect": EffectSpec.gradient("#8b5cf6", "#7c3aed", layer="background"),
    },
    {
        "title": "Conversion",
        "content": "4.2%\n+0.3% MTD",
        "effect": EffectSpec.gradient("#f59e0b", "#d97706", layer="background"),
    },
]

console.frame_group(
    bg_cards,
    layout=LayoutMode.GRID,
    columns=2,
    item_width=30,
    border=Border.ROUNDED,
)
console.newline()

# =============================================================================
# 5. Horizontal Layout for Quick Stats
# =============================================================================

console.rule("[cyan]5. Horizontal Quick Stats Bar[/]")
console.newline()

quick_stats = [
    {"title": "P50", "content": "42ms", "effect": Effect.SUCCESS},
    {"title": "P95", "content": "180ms", "effect": Effect.WARNING},
    {"title": "P99", "content": "450ms", "effect": Effect.ERROR},
]

console.frame_group(
    quick_stats,
    layout=LayoutMode.HORIZONTAL,
    gap=2,
    border=Border.ROUNDED,
)
console.newline()

# =============================================================================
# 6. Mixed Content Dashboard
# =============================================================================

console.rule("[cyan]6. Mixed Content: Alerts + Metrics[/]")
console.newline()

# Alerts section
console.text("[bold]Active Alerts[/]")
alerts = [
    {
        "title": f"{icons.WARNING} Warning",
        "content": "High memory on node-3",
        "effect": Effect.WARNING,
    },
    {
        "title": f"{icons.CROSS_MARK} Critical",
        "content": "Search service down",
        "effect": Effect.ERROR,
    },
]

console.frame_group(
    alerts,
    layout=LayoutMode.HORIZONTAL,
    gap=2,
    border=Border.HEAVY,
)
console.newline()

# Detailed metrics below
console.text("[bold]Node Health[/]")
nodes = [
    {"title": "node-1", "content": f"{icons.CHECK_MARK_BUTTON} Healthy\nCPU: 32%  MEM: 45%", "effect": Effect.SUCCESS},
    {"title": "node-2", "content": f"{icons.CHECK_MARK_BUTTON} Healthy\nCPU: 28%  MEM: 52%", "effect": Effect.SUCCESS},
    {"title": "node-3", "content": f"{icons.WARNING} Warning\nCPU: 45%  MEM: 89%", "effect": Effect.WARNING},
    {"title": "node-4", "content": f"{icons.CHECK_MARK_BUTTON} Healthy\nCPU: 38%  MEM: 61%", "effect": Effect.SUCCESS},
]

console.frame_group(
    nodes,
    layout=LayoutMode.GRID,
    columns=2,
    item_width=35,
    border=Border.ROUNDED,
)
console.newline()

# =============================================================================
# 7. Themed Dashboard (Cyberpunk)
# =============================================================================

console.rule("[cyan]7. Themed Dashboard (Cyberpunk)[/]")
console.newline()

console.banner("NEURAL", font="small", effect=Effect.CYBERPUNK)

cyber_stats = [
    {
        "title": "SYNC",
        "content": "99.7%",
        "effect": EffectSpec.gradient("#ff00ff", "#00ffff", layer="background"),
    },
    {
        "title": "LINK",
        "content": "ACTIVE",
        "effect": EffectSpec.gradient("#00ff00", "#00ffff", layer="background"),
    },
    {
        "title": "POWER",
        "content": "847 TW",
        "effect": EffectSpec.gradient("#ffff00", "#ff00ff", layer="background"),
    },
]

console.frame_group(
    cyber_stats,
    layout=LayoutMode.HORIZONTAL,
    gap=1,
    border=Border.HEAVY,
)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    [
        "Grid Dashboard Patterns:",
        "",
        "  frame_group() options:",
        "    layout=LayoutMode.GRID       - Auto-arrange in grid",
        "    layout=LayoutMode.HORIZONTAL - Side by side",
        "    layout=LayoutMode.VERTICAL   - Stacked (default)",
        "",
        "  Grid options:",
        "    columns=2/3/4/'auto'   - Number of columns",
        "    item_width=30          - Fixed width per item",
        "    gap=1/2                - Space between items",
        "",
        "  Combine with:",
        "    - Background effects for depth",
        "    - Semantic effects for status",
        "    - Banners for section headers",
    ],
    title="Usage Summary",
    effect=Effect.INFO,
    border=Border.DOUBLE,
)
