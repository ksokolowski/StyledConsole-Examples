#!/usr/bin/env python3
"""JSON Schema example - IDE autocomplete for config files.

This example demonstrates how to use the JSON Schema for IDE autocomplete
when writing StyledConsole configuration files in YAML or JSON.

New in v0.10.4!
"""

from styledconsole import Console, get_schema_path, icons

console = Console()

# Get the schema path for IDE configuration
schema_path = get_schema_path()

console.frame(
    [
        f"{icons.GEAR} JSON Schema for IDE Autocomplete",
        "",
        "StyledConsole provides a JSON Schema for validating and",
        "autocompleting YAML/JSON configuration files.",
    ],
    title="JSON Schema Support",
    effect="info",
)
console.newline()

# Show how to configure VS Code
console.frame(
    [
        "Add to your VS Code settings.json:",
        "",
        '"yaml.schemas": {',
        f'  "{schema_path}": ["*.styledconsole.yaml", "*.sc.yaml"]',
        "}",
    ],
    title="VS Code Configuration",
    effect="ocean",
)
console.newline()

# Show inline schema reference
console.frame(
    [
        "Or add inline to your YAML file:",
        "",
        f"# yaml-language-server: $schema={schema_path}",
        "type: frame",
        'title: "My Dashboard"',
        'content: "Hello World!"',
        'effect: "success"',
    ],
    title="Inline Schema Reference",
    effect="forest",
)
console.newline()

# Show the schema path
console.frame(
    [
        "Schema location:",
        str(schema_path),
        "",
        "Get it programmatically:",
        "from styledconsole import get_schema_path",
        "path = get_schema_path()",
    ],
    title="Schema Path",
    effect="gold",
)
console.newline()

# CLI alternative
console.frame(
    [
        "Or use the CLI:",
        "",
        "styledconsole schema           # Show usage info",
        "styledconsole schema --path    # Print path only",
        "styledconsole schema --json    # Print schema JSON",
    ],
    title="CLI Command",
    effect="cyberpunk",
)
