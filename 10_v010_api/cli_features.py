#!/usr/bin/env python3
"""CLI Features demonstration.

This example shows the CLI commands available in StyledConsole v0.10.4.
Run these commands in your terminal to explore StyledConsole features
without writing any code!

New in v0.10.4!
"""

from styledconsole import Console, icons

console = Console()

console.frame(
    [
        f"{icons.ROCKET} StyledConsole CLI",
        "",
        "Explore features without writing code!",
        "Install: pip install styledconsole",
    ],
    title="CLI Preview Tool",
    effect="rainbow",
)
console.newline()

# CLI Commands
commands = [
    {
        "title": "styledconsole demo",
        "content": [
            "Interactive feature showcase",
            "",
            "Shows frames, gradients, icons,",
            "palettes, and more in action.",
        ],
        "effect": "ocean",
    },
    {
        "title": "styledconsole palette [name]",
        "content": [
            "Browse 90 color palettes",
            "",
            "styledconsole palette",
            "styledconsole palette ocean_depths",
        ],
        "effect": "sunset",
    },
    {
        "title": "styledconsole effects [name]",
        "content": [
            "Preview 47 effect presets",
            "",
            "styledconsole effects",
            "styledconsole effects fire",
        ],
        "effect": "fire",
    },
    {
        "title": "styledconsole icons [search]",
        "content": [
            "Search 200+ icons",
            "",
            "styledconsole icons",
            "styledconsole icons rocket",
        ],
        "effect": "mint",
    },
    {
        "title": "styledconsole render <file>",
        "content": [
            "Render YAML/JSON config files",
            "",
            "styledconsole render config.yaml",
            "styledconsole render dashboard.json",
        ],
        "effect": "cyberpunk",
    },
    {
        "title": "styledconsole schema",
        "content": [
            "Get JSON Schema for IDE config",
            "",
            "styledconsole schema --path",
            "styledconsole schema --json",
        ],
        "effect": "gold",
    },
]

for cmd in commands:
    console.frame(
        cmd["content"],
        title=cmd["title"],
        effect=cmd["effect"],
        width=50,
    )
    console.newline()

console.frame(
    [
        "Try it now!",
        "",
        "$ styledconsole demo",
    ],
    title=f"{icons.SPARKLES} Get Started",
    effect="success",
)
