# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

StyledConsole-Examples is the visual laboratory for the StyledConsole ecosystem - a gallery of examples demonstrating terminal formatting, layouts, and best practices.

**Part of:** StyledConsole Ecosystem (see `../CLAUDE.md` for ecosystem overview)
**Depends on:** styledconsole>=0.9.9.5

## Commands

```bash
# Setup
make setup              # Install styledconsole dependency
make check              # Verify styledconsole is installed

# Run Examples
make all                # Run all examples (interactive - pauses between)
make auto               # Run all examples (auto mode - continuous)
make list               # List available categories

# Run by Category (numbered directories)
make quickstart         # 01_quickstart examples
make frames             # 02_frames examples
make content            # 03_content examples
make effects            # 04_effects examples
make banners            # 05_banners examples
make advanced           # 06_advanced examples
make showcases          # 07_showcases examples
make applications       # 08_applications examples
make testing            # 09_testing examples

# Single Example
python 01_quickstart/hello_frame.py
python 04_effects/animation.py
```

## Directory Structure

| Directory | Purpose |
|-----------|---------|
| `01_quickstart/` | Getting started, first frame, basic styling |
| `02_frames/` | Border styles, margins, nested layouts, columns |
| `03_content/` | Tables and content elements |
| `04_effects/` | Gradients, rainbows, palettes, animations |
| `05_banners/` | ASCII art banners and dashboards |
| `06_advanced/` | JSON layouts, render policies |
| `07_showcases/` | Feature demos (emoji, icons, progress) |
| `08_applications/` | Real-world use cases (alerts, menus, logs) |
| `09_testing/` | Validation and stress tests |

## Critical Rules

### Console API Only
- **Never import Rich directly** - Use `from styledconsole import Console`
- **Never access internals** - No `console._rich_console`
- **Use icons facade** - `from styledconsole import icons`

### Modern Effects API (v0.9.9.3+)
```python
from styledconsole import Console, EffectSpec, EFFECTS

console = Console()

# Use effect= parameter (preferred)
console.frame("Content", effect="fire")
console.frame("Content", effect=EFFECTS.ocean)
console.frame("Content", effect=EffectSpec.rainbow(neon=True))

# Use palettes
console.frame("Content", effect=EffectSpec.from_palette("ocean_depths"))
```

### Anti-Patterns
```python
# WRONG: Direct Rich import
from rich.panel import Panel

# WRONG: Accessing internals
console._rich_console.print(...)

# WRONG: Tuple for gradient
console.frame(..., border_color=("red", "blue"))  # Crashes!

# DEPRECATED: Legacy gradient args (still works but prefer effect=)
console.frame(..., border_gradient_start="red", border_gradient_end="blue")

# CORRECT: Use effect parameter
console.frame(..., effect=EffectSpec.gradient("red", "blue", target="border"))
```

## Adding New Examples

1. Place in appropriate numbered category directory
2. Use Console API exclusively with modern `effect=` parameter
3. Use `icons` facade for symbols (provides ASCII fallback)
4. Test with `python <category>/<example>.py`
5. Verify appears in `make list` output
