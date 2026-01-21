#!/usr/bin/env python3
"""Advanced Background Layer Combinations.

Demonstrates complex background effect combinations including:
- Large frames with background gradients
- Multi-stop background gradients
- Background with palette colors
- Nested layouts with background effects
- Dashboard-style compositions with backgrounds

This builds on the basic background_layer.py example with more
visually striking and real-world use cases.
"""

from styledconsole import Console, EffectSpec, RenderPolicy, icons

# Use color-enabled policy
console = Console(policy=RenderPolicy(color=True, unicode=True, emoji=True))

console.frame(
    "Advanced Background Combinations",
    title="Effects Demo",
    effect="rainbow",
)
console.newline()

# =============================================================================
# 1. Large Dashboard with Background Gradient
# =============================================================================

console.rule("[cyan]1. Dashboard with Background Gradient[/]")
console.newline()

# A visually striking large frame with background gradient
dashboard_content = [
    f"{icons.SPARKLES} System Health Dashboard",
    "",
    "  Service          Status      Response    Uptime",
    "  ─────────────────────────────────────────────────",
    f"  {icons.GLOBE_WITH_MERIDIANS} API Gateway     {icons.CHECK_MARK_BUTTON} Online      42ms        99.99%",
    f"  {icons.FILE_CABINET} PostgreSQL      {icons.CHECK_MARK_BUTTON} Online      12ms        99.95%",
    f"  {icons.HIGH_VOLTAGE} Redis Cache     {icons.CHECK_MARK_BUTTON} Online       2ms        99.99%",
    f"  {icons.GEAR} Worker Pool     {icons.WARNING} Scaling     --          98.50%",
    f"  {icons.CLOUD} CDN             {icons.CHECK_MARK_BUTTON} Online      85ms        99.99%",
    "",
    f"  Last updated: 2026-01-20 14:32:15 UTC",
]

console.frame(
    dashboard_content,
    title=f"{icons.BAR_CHART} Production Metrics",
    effect=EffectSpec.gradient("#1e3a5f", "#2d5a87", layer="background"),
    border="heavy",
    width=60,
)
console.newline()

# =============================================================================
# 2. Multi-Stop Background Gradient
# =============================================================================

console.rule("[cyan]2. Multi-Stop Background Gradient[/]")
console.newline()

# Sunset-inspired multi-stop gradient on background
sunset_bg = EffectSpec.multi_stop(
    ["#ff6b6b", "#feca57", "#ff9ff3", "#54a0ff"],
    layer="background",
    direction="horizontal",
)

console.frame(
    [
        "Multi-stop gradients create",
        "smooth color transitions",
        "across multiple colors.",
        "",
        "This sunset uses 4 colors:",
        "coral → gold → pink → blue",
    ],
    title="Sunset Background",
    effect=sunset_bg,
    border="double",
    width=40,
)
console.newline()

# Aurora-inspired multi-stop
aurora_bg = EffectSpec.multi_stop(
    ["#00d9ff", "#00ff87", "#b8ff00", "#00d9ff"],
    layer="background",
    direction="diagonal",
)

console.frame(
    [
        "Northern Lights Effect",
        "",
        "Diagonal gradient flowing",
        "from corner to corner",
        "with aurora colors.",
    ],
    title="Aurora Background",
    effect=aurora_bg,
    border="rounded",
    width=40,
)
console.newline()

# =============================================================================
# 3. Background with Palette Colors
# =============================================================================

console.rule("[cyan]3. Palette-Based Backgrounds[/]")
console.newline()

# Different palettes for different contexts
palettes_demo = [
    ("ocean_depths", "Deep Ocean", "Calm, professional"),
    ("cyberpunk_neon", "Cyber Neon", "Bold, futuristic"),
    ("forest_green", "Forest", "Natural, organic"),
]

for palette_name, title, description in palettes_demo:
    effect = EffectSpec.from_palette(palette_name, layer="background")
    console.frame(
        description,
        title=title,
        effect=effect,
        border="rounded",
        width=35,
    )

console.newline()

# =============================================================================
# 4. Alert Boxes with Background Severity
# =============================================================================

console.rule("[cyan]4. Alert Boxes with Background Severity[/]")
console.newline()

alerts = [
    ("success", "#10b981", "#065f46", f"{icons.CHECK_MARK_BUTTON} Deployment successful"),
    ("warning", "#f59e0b", "#92400e", f"{icons.WARNING} High memory usage detected"),
    ("error", "#ef4444", "#991b1b", f"{icons.CROSS_MARK} Connection to primary DB failed"),
    ("info", "#3b82f6", "#1e40af", f"{icons.INFORMATION} Scheduled maintenance tonight"),
]

for alert_type, start_color, end_color, message in alerts:
    effect = EffectSpec.gradient(start_color, end_color, layer="background")
    console.frame(
        message,
        title=alert_type.upper(),
        effect=effect,
        border="heavy",
        width=50,
    )

console.newline()

# =============================================================================
# 5. Card Grid with Background Effects
# =============================================================================

console.rule("[cyan]5. Card Grid with Background Effects[/]")
console.newline()

# Simulate a metrics dashboard with cards
console.text("[bold]Server Metrics (Background Gradients):[/]")
console.newline()

# Using frame_group with background effects on each item
metrics = [
    {"title": "CPU", "content": "45%", "colors": ("#22c55e", "#16a34a")},
    {"title": "Memory", "content": "78%", "colors": ("#eab308", "#ca8a04")},
    {"title": "Disk", "content": "32%", "colors": ("#3b82f6", "#2563eb")},
    {"title": "Network", "content": "1.2 GB/s", "colors": ("#8b5cf6", "#7c3aed")},
]

# Create individual frames with background gradients
for metric in metrics:
    effect = EffectSpec.gradient(
        metric["colors"][0], metric["colors"][1], layer="background"
    )
    console.frame(
        [metric["content"], ""],
        title=metric["title"],
        effect=effect,
        border="rounded",
        width=20,
        align="center",
    )

console.newline()

# =============================================================================
# 6. Neon Background with Cyberpunk Aesthetic
# =============================================================================

console.rule("[cyan]6. Neon Cyberpunk Background[/]")
console.newline()

neon_bg = EffectSpec.rainbow(neon=True, layer="background", direction="diagonal")

console.frame(
    [
        "╔══════════════════════════════════════╗",
        "║     NEURAL INTERFACE ACTIVE          ║",
        "║                                      ║",
        "║   > System Status: ONLINE            ║",
        "║   > Connection: ENCRYPTED            ║",
        "║   > Firewall: MAXIMUM                ║",
        "║                                      ║",
        "║   Press [ENTER] to continue...       ║",
        "╚══════════════════════════════════════╝",
    ],
    title="CYBERSPACE",
    effect=neon_bg,
    border="heavy",
    width=50,
)
console.newline()

# =============================================================================
# 7. Comparison: Foreground vs Background on Same Content
# =============================================================================

console.rule("[cyan]7. Side-by-Side: Foreground vs Background[/]")
console.newline()

content = [
    "The same gradient applied",
    "to foreground (text color)",
    "vs background creates",
    "very different effects.",
]

console.text("[bold]Foreground gradient (text colored):[/]")
console.frame(
    content,
    effect=EffectSpec.gradient("magenta", "cyan", layer="foreground"),
    border="rounded",
    width=40,
)
console.newline()

console.text("[bold]Background gradient (background colored):[/]")
console.frame(
    content,
    effect=EffectSpec.gradient("magenta", "cyan", layer="background"),
    border="rounded",
    width=40,
)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    [
        "Background Layer Tips:",
        "",
        "  1. Use darker colors for readability",
        "  2. Multi-stop gradients create depth",
        "  3. Horizontal works great for wide frames",
        "  4. Diagonal adds dynamic feel",
        "  5. Pair with heavy/double borders",
        "",
        "API:",
        '  EffectSpec.gradient(..., layer="background")',
        '  EffectSpec.rainbow(..., layer="background")',
        '  EffectSpec.from_palette(..., layer="background")',
    ],
    title="Usage Tips",
    effect=EffectSpec.gradient("#1e293b", "#334155", layer="background"),
    border="double",
)
