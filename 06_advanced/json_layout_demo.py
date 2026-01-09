"""
Declarative Layout Demo
======================

Demonstrates building a complete CLI dashboard from a single JSON-like structure.
This pattern enables "Low Code" interface construction.

NOTE: This example requires the experimental presets module which is under development.
"""

from io import StringIO

from styledconsole import Console, EffectSpec, cycle_phase, icons
from styledconsole.animation import Animation


def run_demo():
    """Demonstrate declarative-style layouts using Console API."""
    console = Console()

    # Header
    console.banner(
        "MISSION CONTROL",
        effect=EffectSpec.rainbow(),
        border="heavy",
    )

    console.frame("Orbital Station Alpha", border="minimal", border_color="cyan", align="center", frame_align="center")
    console.rule(style="cyan dim")
    console.newline()

    # 2. Data section with frame
    system_status = [
        f"{icons.GEAR} Life Support:     NOMINAL",
        f"{icons.SATELLITE_ANTENNA} Navigation:       CALIBRATING",
        f"{icons.HIGH_VOLTAGE} Power Systems:    98%",
    ]

    console.frame(
        system_status,
        title="System Status",
        border="rounded",
        effect=EffectSpec.gradient("cyan", "blue"),
        frame_align="center",
    )

    console.newline()

    # 3. Animated Alert panel with solid red frame and cycling text colors
    console.rule("ALERTS", color="red")
    console.newline()

    def alert_frames():
        # Cycle through warning colors for the text
        # Using explicit hex to remove naming ambiguity and avoiding pure yellow
        # (which can look like white in some terminal themes).
        # Sequence: Red -> OrangeRed -> Orange -> DarkOrange -> Gold
        colors = ["#FF0000", "#FF4500", "#FFA500", "#FF8C00", "#FFD700", "#FF8C00", "#FFA500", "#FF4500"]
        color_index = 0
        
        from styledconsole.policy import RenderPolicy
        # Force a policy with all features enabled for the animation buffer
        anim_policy = RenderPolicy(color=True, unicode=True, emoji=True)
        
        # Get actual width for centering the animation frames
        target_width = console._rich_console.width

        for _ in range(60):
            buffer = StringIO()
            temp_console = Console(
                file=buffer, 
                width=target_width, 
                record=True, 
                policy=anim_policy, 
                detect_terminal=False
            )

            current_color = colors[color_index % len(colors)]
            
            # Using content_color parameter for guaranteed color application
            # and frame_align="center" to match the rest of the layout
            temp_console.frame(
                f"{icons.WARNING} Proximity Warning: Asteroid Field Detected",
                title="Alerts",
                border="rounded",
                border_color="red",
                content_color=current_color,
                padding=1,
                frame_align="center",
            )

            yield buffer.getvalue()
            color_index += 1

    Animation.run(alert_frames(), fps=10, duration=6)


if __name__ == "__main__":
    run_demo()
