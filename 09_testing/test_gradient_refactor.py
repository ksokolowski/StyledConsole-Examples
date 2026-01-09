#!/usr/bin/env python3
"""
Gradient Refactor Validation
============================

Tests gradient rendering with the modern effect= API.
Validates vertical, horizontal, and rainbow gradients.
"""

from styledconsole import THEMES, Console, EffectSpec


def test_gradients():
    console = Console()

    print("\n=== VALIDATION: Gradient API Test ===\n")

    # 1. Vertical Gradient (Content)
    print("1. Vertical Content Gradient (Red -> Blue)")
    console.frame(
        "Line 1\nLine 2\nLine 3\nLine 4",
        border="rounded",
        effect=EffectSpec.gradient("red", "blue", direction="vertical"),
        title="Vertical Content",
    )

    # 2. Horizontal Gradient (Content)
    print("\n2. Horizontal Content Gradient (Green -> Yellow)")
    console.frame(
        "This text has a horizontal gradient applied",
        border="rounded",
        effect=EffectSpec.gradient("green", "yellow", direction="horizontal"),
        title="Horizontal Content",
    )

    # 3. Rainbow effect
    print("\n3. Rainbow Effect")
    console.frame(
        "Rainbow content across multiple lines\nLine 2\nLine 3",
        border="rounded",
        effect=EffectSpec.rainbow(),
        title="Rainbow Effect",
    )

    # 4. Using preset theme
    print("\n4. Preset Theme (RAINBOW)")
    themed_console = Console(theme=THEMES.RAINBOW)
    themed_console.frame("Content with RAINBOW theme", title="Theme-based Gradient")

    # 5. Border gradient via effect
    print("\n5. Border-only gradient")
    console.frame(
        "Plain content",
        border="double",
        effect=EffectSpec.gradient("cyan", "magenta", target="border"),
        title="Border Gradient",
    )

    print("\n✅ All gradient tests passed!")


if __name__ == "__main__":
    test_gradients()
