#!/usr/bin/env python3
"""
Animated Gradients Demo
======================

Demonstrates animated gradients using the high-level phase API.
This example shows cycling rainbow effects on frame borders using
the declarative EffectSpec system with phase parameter.

For production progress bars, use Console.progress() instead.
"""

from io import StringIO

from styledconsole import Console, cycle_phase
from styledconsole.animation import Animation
from styledconsole.effects import EffectSpec


def create_animated_banner():
    """Demonstrate animated rainbow banner using phase parameter."""
    console = Console()

    print("🎨 Animation Demo - Rainbow Banner")
    print("=" * 50)

    # Generate frames by cycling phase through full cycle
    def frames():
        phase = 0.0
        # 30 frames for smooth animation (one full color cycle)
        for _ in range(90):  # Loop 3 times (3 × 30 frames)
            buffer = StringIO()
            temp_console = Console(file=buffer, record=True)

            temp_console.frame(
                [
                    "✨ Animated Gradients ✨",
                    "",
                    f"Phase: {phase:.2f}",
                    "",
                    "Watch the colors cycle!",
                ],
                title="🚀 Animation Demo",
                border="double",
                width=40,
                effect=EffectSpec.rainbow(phase=phase, direction="diagonal"),
            )

            yield buffer.getvalue()
            phase = cycle_phase(phase)

    Animation.run(frames(), fps=10, duration=9)


def create_progress_animation():
    """Show animated progress-style display."""
    console = Console()

    print("\n📊 Progress Animation Demo")
    print("=" * 50)

    def frames():
        stages = [
            ("Initializing...", "cyan", 0),
            ("Loading modules...", "blue", 20),
            ("Connecting...", "purple", 40),
            ("Processing...", "magenta", 60),
            ("Finalizing...", "pink", 80),
            ("Complete!", "green", 100),
        ]

        for stage, color, progress in stages:
            buffer = StringIO()
            temp_console = Console(file=buffer, record=True)

            bar = "█" * (progress // 10) + "░" * (10 - progress // 10)
            content = [
                f"Status: {stage}",
                "",
                f"Progress: [{bar}] {progress}%",
            ]

            temp_console.frame(
                content,
                title="🔄 Task Progress",
                border="rounded",
                border_color=color,
                width=45,
            )

            # Each stage shows for longer
            for _ in range(5):
                yield buffer.getvalue()

    Animation.run(frames(), fps=5, duration=6)


def main():
    print("=" * 60)
    print("  STYLEDCONSOLE ANIMATION DEMO")
    print("=" * 60)
    print()

    try:
        create_animated_banner()
        create_progress_animation()
    except KeyboardInterrupt:
        print("\nAnimation stopped.")

    print("\n✅ Animation demo complete!")
    print("Tip: Use Console.progress() for production progress bars.")


if __name__ == "__main__":
    main()
