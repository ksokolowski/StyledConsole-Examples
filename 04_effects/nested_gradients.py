#!/usr/bin/env python3
"""
🏛️ Nested Gradient Architecture Showcase

Demonstrates the power of StyledConsole's rendering engine by nesting
multiple frames with independent gradient borders using the modern effect= API.

Structure:
1. Fire Layer (Outer)
2. Growth Layer
3. Depth Layer
4. Soul Layer (Inner)
"""

from styledconsole import Console, EffectSpec

console = Console()


def main():
    console.clear()
    console.newline(2)

    # 4. Soul Layer (Innermost)
    # Meaning: The core essence
    soul_content = "This is gradient architecture at its finest."
    soul_frame = console.render_frame(
        soul_content,
        border="double",
        align="center",
        width=50,
        padding=1,
        effect=EffectSpec.gradient(
            "#E6E6FA",  # Lavender
            "#9370DB",  # Medium Purple
            direction="vertical",
            target="border"
        ),
    )

    # 3. Depth Layer
    # Meaning: Complexity and understanding
    depth_frame = console.render_frame(
        [
            "Four gradient layers, each with meaning:",
            "Fire → Growth → Depth → Soul",
            "",
            soul_frame,
        ],
        border="rounded",
        align="center",
        width=58,
        padding=1,
        effect=EffectSpec.gradient(
            "#4169E1",  # Royal Blue
            "#000080",  # Navy
            direction="vertical",
            target="border"
        ),
    )

    # 2. Growth Layer
    # Meaning: Expansion and development
    growth_frame = console.render_frame(
        [
            "Native Implementation",
            "Rendering Engine v0.5.0",
            "",
            depth_frame,
        ],
        border="thick",
        align="center",
        width=66,
        padding=1,
        effect=EffectSpec.gradient(
            "#90EE90",  # Light Green
            "#006400",  # Dark Green
            direction="vertical",
            target="border"
        ),
    )

    # 1. Fire Layer (Outermost)
    # Meaning: Passion and energy
    # Render and print the final result
    console.frame(
        [
            "🌈 NESTED GRADIENT ARCHITECTURE",
            "",
            growth_frame,
        ],
        title="🏛️  Gradient Architecture",
        border="heavy",
        align="center",
        width=76,
        padding=2,
        effect=EffectSpec.gradient(
            "#FF4500",  # Orange Red
            "#8B0000",  # Dark Red
            direction="vertical",
            target="border"
        ),
    )

    console.newline(2)


if __name__ == "__main__":
    main()
