"""
Declarative Layout Demo
======================

Demonstrates building a complete CLI dashboard from a single JSON-like structure.
This pattern enables "Low Code" interface construction.

NOTE: This example requires the experimental presets module which is under development.
"""

from styledconsole import Console, EffectSpec


def run_demo():
    """Demonstrate declarative-style layouts using Console API."""
    console = Console()

    # Header
    console.banner(
        "MISSION CONTROL",
        effect=EffectSpec.rainbow(),
        border="heavy",
    )

    console.frame("Orbital Station Alpha", border="minimal", border_color="cyan", align="center")
    console.rule(style="cyan dim")
    console.newline()

    # 2. Data section with frame
    system_status = [
        "⚙️  Life Support:     NOMINAL",
        "📡 Navigation:       CALIBRATING",
        "🔋 Power Systems:    98%",
    ]

    console.frame(
        system_status,
        title="System Status",
        border="rounded",
        effect=EffectSpec.gradient("cyan", "blue"),
    )

    console.newline()

    # 3. Alert panel
    console.frame(
        "⚠ Proximity Warning: Asteroid Field Detected",
        title="Alerts",
        border="rounded",
        border_color="red",
        padding=1,
    )


if __name__ == "__main__":
    run_demo()
