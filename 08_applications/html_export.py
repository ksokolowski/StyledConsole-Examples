#!/usr/bin/env python3
"""
HTML Export Demo
===============

Demonstrates exporting a rich dashboard to HTML with custom styling and gradients.
Uses Console.export_html() facade - no internal API access needed.
"""

import os

from styledconsole import Console, EffectSpec


def create_dashboard(console: Console) -> None:
    """Render a complex dashboard to the console."""

    # 1. Gradient Banner
    console.banner(
        "SYSTEM STATUS",
        effect=EffectSpec.gradient("dodgerblue", "cyan"),
        border="double",
        align="center",
    )

    # 2. Status Grid
    metrics_lines = [
        "CPU Load      42%        🟢",
        "Memory        1.2GB      🟢",
        "Disk          85%        ⚠️",
        "Network       120ms      🔴",
    ]

    # 3. Framed Content with Metrics
    console.frame(
        metrics_lines,
        title="Metrics",
        border="rounded",
        border_color="blue",
        title_color="cyan",
    )

    # 4. Gradient Text
    console.text("System analysis complete. No critical errors found.", color="green")


def main():
    # Initialize console with recording enabled
    console = Console(record=True, width=100)

    print("Rendering dashboard...")
    create_dashboard(console)

    output_file = "results/dashboard_export.html"

    print(f"Exporting to {output_file}...")

    # Export using Console.export_html() facade
    html = console.export_html(inline_styles=True)

    # Add custom styling including page title
    custom_css = """
    <title>System Status Dashboard</title>
    <style>
    body {
        font-family: 'Fira Code', monospace;
        background-color: #1a1a1a;
        margin: 2rem;
    }
    .rich-terminal {
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        border-radius: 8px;
        padding: 2rem;
        background-color: #222;
    }
    </style>
    """
    html = html.replace("</head>", custom_css + "\n</head>")

    # Ensure results directory exists
    os.makedirs("results", exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Export complete! Open {output_file} in your browser.")
    print(f"File path: {os.path.abspath(output_file)}")


if __name__ == "__main__":
    main()
