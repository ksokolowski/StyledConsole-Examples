#!/usr/bin/env python3
"""
Gradient Table Example
=====================

Demonstrates how to apply gradient effects to a GradientTable with heavy borders,
creating a premium "cyberpunk" or "high-tech" look.

Features:
- Heavy border style (including internal separators)
- Gradient applied ONLY to borders (diagonal)
- Rich text styling (bold, italic, colored) for content
- Icons integration
"""

from styledconsole import Console, icons
from styledconsole.policy import RenderPolicy
from styledconsole.presets.tables import GradientTable


def render_gradient_table() -> None:
    """Render a table with heavy borders and apply a gradient filter."""
    # Initialize Console with a policy that ensures Rich Features are enabled
    console = Console(policy=RenderPolicy(unicode=True, color=True))

    console.print("\n[bold]Gradient Table Demo[/bold]")
    console.print(
        "Applying gradients to heavy table borders while keeping content distinct.\n"
    )

    # Create the GradientTable with gradient parameters
    # GradientTable uses border_gradient_start/end parameters
    table = GradientTable(
        title="[bold italic white]SYSTEM DIAGNOSTICS[/]",
        border_style="heavy",
        border_gradient_start="cyan",
        border_gradient_end="magenta",
        border_gradient_direction="diagonal",
        padding=(0, 2),
    )

    # Add columns with different styles for content
    table.add_column("COMPONENT", style="bold cyan", no_wrap=True)
    table.add_column("STATUS", style="bold")
    table.add_column("METRICS", justify="right", style="italic blue")
    table.add_column("LAST UPDATE", justify="right", style="dim white")

    # Add rows with icons and mixed content styles
    table.add_row(
        f"{icons.GEAR} Core Processing",
        f"[green]{icons.CHECK_MARK_BUTTON} OPERATIONAL[/]",
        "24% Load",
        "10ms ago",
    )

    table.add_row(
        f"{icons.FLOPPY_DISK} Storage Array",
        f"[yellow]{icons.WARNING} DEGRADED[/]",
        "89% Full",
        "45ms ago",
    )

    table.add_row(
        f"{icons.SATELLITE_ANTENNA} Uplink Module",
        f"[red]{icons.CROSS_MARK} OFFLINE[/]",
        "0 bps",
        "2s ago",
    )

    table.add_row(
        f"{icons.SHIELD} Security Grid",
        f"[green]{icons.LOCKED} SECURE[/]",
        "No Threats",
        "120ms ago",
    )

    # Print directly - GradientTable handles gradient application
    console.print(table)

    console.print("\n[dim]Note: Gradient applied to 'heavy' border characters only.[/]\n")


if __name__ == "__main__":
    render_gradient_table()
