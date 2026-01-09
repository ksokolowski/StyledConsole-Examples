#!/usr/bin/env python3
"""First Banner - Create ASCII art text.

Learn how to create eye-catching ASCII art banners
with gradients and borders.

Usage:
    python 01_quickstart/first_banner.py
"""

from styledconsole import Console, EffectSpec

console = Console()

# Simple banner with default font
console.banner("HELLO")

console.newline()

# Banner with gradient colors
console.banner(
    "SUCCESS",
    effect=EffectSpec.gradient("green", "cyan"),
    border="rounded",
)

console.newline()

# Banner with different font
console.banner(
    "COOL",
    font="slant",
    effect=EffectSpec.gradient("magenta", "blue"),
)
