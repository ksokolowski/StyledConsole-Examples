#!/usr/bin/env python3
"""
StyledTable Demo
===============

Demonstrates the capabilities of the StyledTable class, including policy-aware rendering
and seamless integration with styling features.
"""

from styledconsole import Console, icons
from styledconsole.policy import RenderPolicy
from styledconsole.table import StyledTable


def demonstrate_table(console: Console, policy: RenderPolicy, title: str) -> None:
    """Helper to render a table with a specific policy."""
    console.print(f"\n[bold cyan]=== {title} ===[/]")
    console.print(f"[dim]Policy: unicode={policy.unicode}, emoji={policy.emoji}[/]")

    # These scenarios force explicit policies to SIMULATE other
    # environments; when a scenario enables more than the detected
    # terminal supports, its rendering may legitimately look off here.
    detected = RenderPolicy.from_env()
    if (policy.emoji and not detected.emoji) or (policy.unicode and not detected.unicode):
        console.print(
            "[dim italic]note: simulated environment — this scenario forces "
            "capabilities your terminal may not render faithfully[/]"
        )
    console.print()

    table = StyledTable(
        title=f"{icons.GLOBE_WITH_MERIDIANS} Server Cluster Status",
        policy=policy,
        border_style="rounded",
        show_lines=True,
    )

    table.add_column("Service", style="cyan", no_wrap=True)
    table.add_column("Region", style="blue")
    table.add_column("Status", style="magenta")
    table.add_column("Uptime", justify="right", style="green")

    # Add rows with emojis
    # Note: If policy.emoji=True, icons render as emojis.
    #       If policy.emoji=False, icons rendering mechanism (in styledconsole.icons) 
    #       handles fallback, AND StyledTable provides an extra layer of 
    #       sanitization for raw strings containing emojis (like "🟢 Online").
    
    table.add_row(
        f"{icons.CLOUD} API Gateway", 
        "us-east-1", 
        f"{icons.GREEN_CIRCLE} Online",
        "99.9%"
    )
    table.add_row(
        f"{icons.FILE_CABINET} Primary DB", 
        "us-east-1", 
        f"{icons.YELLOW_CIRCLE} Maintenance",
        "98.5%"
    )
    table.add_row(
        f"{icons.HIGH_VOLTAGE} Cache Layer", 
        "us-west-2", 
        f"{icons.GREEN_CIRCLE} Online", 
        "99.9%"
    )
    
    # Example of status display with styled text
    # Using inline styling for critical status
    status_text = "[bold white on red] CRITICAL [/]"
    
    table.add_row(
        f"{icons.GEAR} Worker Pool", 
        "eu-central-1", 
        status_text, 
        "0.0%"
    )

    console.print(table)


def run_demo() -> None:
    """Run the demonstration."""
    console = Console()
    
    console.print("[bold green]StyledTable Capabilities Demo[/]")
    console.print("Demonstrating how StyledTable adapts to different environments.\n")

    # Scenario 1: Full Capability (Modern Terminal)
    policy_full = RenderPolicy(unicode=True, emoji=True, color=True)
    demonstrate_table(console, policy_full, "Scenario 1: Full Features (Modern Terminal)")

    # Scenario 2: CI Environment (Unicode enabled, but no Emoji)
    # Browsers/CI logs often support borders but have issues with color emoji widths usually
    policy_ci = RenderPolicy(unicode=True, emoji=False, color=True)
    demonstrate_table(console, policy_ci, "Scenario 2: CI Mode (Unicode Yes, Emoji No)")

    # Scenario 3: Legacy Terminal (No Unicode, No Emoji)
    policy_legacy = RenderPolicy(unicode=False, emoji=False, color=True)
    demonstrate_table(console, policy_legacy, "Scenario 3: Legacy Mode (ASCII Borders)")


if __name__ == "__main__":
    run_demo()
