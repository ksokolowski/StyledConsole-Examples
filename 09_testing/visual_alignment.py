#!/usr/bin/env python3
"""
Visual Alignment Test

Automated tests for visual alignment across all border styles, exercised
through the public Console API — every line of a rendered frame must have
the exact same visual width, emoji content included.
"""

from styledconsole import Console, visual_width
from styledconsole.utils.text import strip_ansi

console = Console()

print()
print("=" * 80)
print("VISUAL ALIGNMENT TESTING")
print("=" * 80)
print()

# Test configuration
TEST_WIDTH = 60
TEST_CASES = [
    ("Plain text", "left"),
    ("🚀 Emoji at start", "left"),
    ("Emoji at end 🎉", "right"),
    ("🔥 Multiple 🎯 emojis 🌟", "center"),
    ("Mix of text and 🎨 emoji", "center"),
]

STYLES = ["solid", "double", "rounded", "heavy", "thick", "ascii", "minimal", "dots"]

# Track results
total_tests = 0
passed_tests = 0
failed_tests = []

print(f"Testing {len(STYLES)} styles × {len(TEST_CASES)} test cases")
print(f"Expected width for all frame lines: {TEST_WIDTH}")
print()

for style_name in STYLES:
    print(f"Testing {style_name} style...")
    style_passed = True

    for content, align in TEST_CASES:
        rendered = console.render_frame(
            content, title="Test", border=style_name, width=TEST_WIDTH, align=align
        )
        for line in rendered.splitlines():
            if not line.strip():
                continue
            total_tests += 1
            width = visual_width(line)
            if width == TEST_WIDTH:
                passed_tests += 1
            else:
                style_passed = False
                failed_tests.append(
                    {
                        "style": style_name,
                        "content": content,
                        "expected": TEST_WIDTH,
                        "actual": width,
                        "line": strip_ansi(line),
                    }
                )

    if style_passed:
        print(f"  ✅ {style_name}: All tests passed")
    else:
        print(f"  ❌ {style_name}: Some tests failed")
    print()

# Display summary
print("=" * 80)
print("TEST SUMMARY")
print("=" * 80)
print()

print(f"Total tests: {total_tests}")
print(f"Passed: {passed_tests} ({100 * passed_tests / total_tests:.1f}%)")
print(f"Failed: {len(failed_tests)}")
print()

if failed_tests:
    print("FAILURES:")
    print()
    for i, failure in enumerate(failed_tests, 1):
        print(f"{i}. {failure['style']}")
        print(f"   Content: '{failure['content']}'")
        print(f"   Expected width: {failure['expected']}, Actual: {failure['actual']}")
        print(f"   Line: {failure['line']}")
        print()
    raise SystemExit(1)

print("🎉 ALL TESTS PASSED! 🎉")
print()
print("Visual alignment is perfect across:")
print(f"  • {len(STYLES)} border styles")
print(f"  • {len(TEST_CASES)} test cases with emojis")
print()
print("✨ Emoji-safe rendering is working flawlessly! ✨")

print()
print("=" * 80)

# Visual demonstration
print()
print("VISUAL DEMONSTRATION")
print("=" * 80)
print()

demo_lines = [
    "Plain ASCII text",
    "🚀 Emoji at start",
    "Emoji at end 🎉",
    "🔥 Center aligned 🌟",
    "",
    *(f"{content} ({align})" for content, align in TEST_CASES),
]
console.frame(demo_lines, title="🎨 Perfect Alignment Demo", border="rounded", width=55)
print()
