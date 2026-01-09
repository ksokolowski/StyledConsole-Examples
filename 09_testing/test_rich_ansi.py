#!/usr/bin/env python3
"""
ANSI Color Handling Test
========================

Tests that StyledConsole correctly handles ANSI-colored text
within frames and other elements.
"""

from styledconsole import Console


def test_ansi_handling():
    """Test ANSI color codes within StyledConsole elements."""
    console = Console()

    print("--- Test: ANSI Color Handling in StyledConsole ---")
    print()

    # Test 1: Pre-colored text in frames
    print("Test 1: Pre-colored ANSI text in frame")
    console.frame(
        [
            "\033[31mRed text\033[0m",
            "\033[32mGreen text\033[0m",
            "\033[34mBlue text\033[0m",
        ],
        title="ANSI Colors",
        border="rounded",
    )

    # Test 2: Mixed styled content
    print("\nTest 2: Mixed styled content")
    console.frame(
        [
            "\033[1mBold\033[0m and \033[3mitalic\033[0m text",
            "\033[4mUnderlined\033[0m and \033[9mstrikethrough\033[0m",
            "Plain text with \033[33myellow\033[0m word",
        ],
        title="Mixed Styles",
        border="rounded",
    )

    # Test 3: Verify Console styled text
    print("\nTest 3: Console styled text methods")
    console.text("This is red", color="red")
    console.text("This is bold green", color="green", bold=True)
    console.text("This is italic blue", color="blue", italic=True)

    print("\n✅ ANSI handling tests complete!")
    print("Visual inspection: Colors should render correctly above.")


if __name__ == "__main__":
    test_ansi_handling()
