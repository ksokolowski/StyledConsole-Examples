# StyledConsole Examples

This repository is a visual laboratory for [StyledConsole](https://github.com/ksokolowski/StyledConsole). It demonstrates rich terminal features, advanced layouts, and best practices for creating beautiful command-line interfaces.

**Latest Updates:**
- ✅ Reorganized into 9 numbered categories
- ✅ Updated to use modern `effect=` API (v0.9.9.4+)
- ✅ Integrated 90 curated color palettes
- ✅ Support for 1,347 color names (CSS4 + Rich + Extended)
- ✅ Removed deprecated API usage

## 🚀 Getting Started

### Quick Start

```bash
# Install dependencies
make setup

# List available categories
make list

# Run all examples
make all

# Run specific category
make quickstart
make effects
make banners
```

### Manual Execution

```bash
# Run a single example (using StyledConsole environment)
cd ../StyledConsole
uv run python ../StyledConsole-Examples/01_quickstart/hello_frame.py
```

## 📂 Repository Structure

```
StyledConsole-Examples/
├── 01_quickstart/      # 🚀 Getting Started (3 examples)
│   ├── basic_styling.py
│   ├── first_banner.py
│   └── hello_frame.py
│
├── 02_frames/          # 🖼️ Frame System (4 examples)
│   ├── all_border_styles.py
│   ├── margins_demo.py
│   ├── nested_frames.py
│   └── styles_demo.py
│
├── 03_content/         # 📝 Content Elements (1 example)
│   └── table_demo.py
│
├── 04_effects/         # 🌈 Visual Effects (7 examples)
│   ├── animation.py
│   ├── colorhex_showcase.py
│   ├── custom_palette_import.py
│   ├── effect_showcase.py
│   ├── gradient_table.py
│   ├── nested_gradients.py
│   └── rainbow_cycling.py
│
├── 05_banners/         # 🔤 ASCII Banners (2 examples)
│   ├── dashboard.py
│   └── welcome_screens.py
│
├── 06_advanced/        # ⚙️ Advanced Features (3 examples)
│   ├── json_layout_demo.py
│   ├── json_table_demo.py
│   └── render_policy_demo.py
│
├── 07_showcases/       # ✨ Feature Showcases (3 examples)
│   ├── emoji_integration_demo.py
│   ├── icon_provider_demo.py
│   └── progress_demo.py
│
├── 08_applications/    # 💼 Real-World Applications (8 examples)
│   ├── alerts.py
│   ├── cli_menus.py
│   ├── data_tables.py
│   ├── html_export.py
│   ├── logs_viewer.py
│   ├── notifications.py
│   ├── progress_dashboard.py
│   └── status_panels.py
│
└── 09_testing/         # 🧪 Testing & Validation (17 examples)
    ├── benchmark.py
    ├── emoji_comparison.py
    ├── test_*.py (various tests)
    ├── visual_alignment.py
    └── visual_stress_test.py
```

## 📖 Key Examples

### Modern Effect System

```python
from styledconsole import Console, EffectSpec

console = Console()

# Gradient effect
console.banner("HELLO", effect=EffectSpec.gradient("cyan", "magenta"))

# Palette-based effect
console.frame(
    "Using ocean depths palette",
    effect=EffectSpec.from_palette("ocean_depths"),
)

# Rainbow effect
console.banner("RAINBOW", effect=EffectSpec.rainbow())
```

### Core Features

```bash
# All border styles
make frames

# Icon and emoji integration
make showcases

# Real-world applications
make applications
```

## 🎮 Running Examples

### Interactive Mode (default)

```bash
python run_examples.py
```

Press Enter between each example for visual inspection.

### Auto Mode

```bash
python run_examples.py --auto
```

Runs all examples without pauses.

### Fast Mode

```bash
python run_examples.py --fast
```

Skips testing examples (09_testing).

### Specific Categories

```bash
python run_examples.py --categories 01_quickstart,04_effects
```

## 🧪 Development

This repository is designed to work alongside the main StyledConsole repository:

```
workspace/
├── StyledConsole/           # Main library
├── StyledConsole-Examples/  # This repository
└── StyledConsole-Internal/  # Planning docs
```

## ⚖️ License

This project is licensed under the Apache 2.0 License.
