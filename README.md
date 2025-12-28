# StyledConsole Examples

This repository is a visual laboratory and museum for [StyledConsole](https://github.com/ksokolowski/StyledConsole). It demonstrates rich terminal features, advanced layouts, and best practices for creating beautiful command-line interfaces.

## 🚀 Getting Started

### Quick Start

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ksokolowski/StyledConsole-Examples.git
   cd StyledConsole-Examples
   ```

2. **Install dependencies:**

   ```bash
   make setup
   # or
   pip install styledconsole
   ```

3. **Run examples:**

   **Option A: Run all examples interactively**

   ```bash
   python run_examples.py
   # or
   make all
   ```

   **Option B: Run all examples in auto mode (no pauses)**

   ```bash
   python run_examples.py --auto
   # or
   make auto
   ```

   **Option C: Run specific categories**

   ```bash
   python run_examples.py --categories core,frames
   # or
   make core
   make usecases
   ```

   **Option D: Run a single example**

   ```bash
   python banners/welcome_screens.py
   # or with uv
   uv run banners/welcome_screens.py
   ```

## 📖 Examples Runner

The repository includes a robust examples runner ([run_examples.py](run_examples.py)) that organizes and executes all examples by category:

```bash
# List all available categories
python run_examples.py --list

# Run specific categories
python run_examples.py --categories core,usecases

# Auto mode (no pauses)
python run_examples.py --auto

# Fast mode (skip validation examples)
python run_examples.py --fast
```

### Available Commands

| Command           | Description                        |
| ----------------- | ---------------------------------- |
| `make all`        | Run all examples (interactive)     |
| `make auto`       | Run all examples (auto mode)       |
| `make fast`       | Run all examples (skip validation) |
| `make list`       | List available categories          |
| `make core`       | Run core feature examples          |
| `make frames`     | Run frame system examples          |
| `make gradients`  | Run gradient effect examples       |
| `make banners`    | Run banner examples                |
| `make usecases`   | Run use case examples              |
| `make validation` | Run validation examples            |

## 📂 Repository Structure

- **`banners/`**: High-impact visual headers and large-scale terminal art.
- **`frames/`**: Demonstrations of borders, padding, margins, and complex layout nesting.
- **`gradients/`**: Rainbow effects and linear color transitions for text and borders.
- **`usecases/`**: Complex real-world components like CLI menus, dashboards, and log viewers.
- **`validation/`**: Stress tests and terminal compatibility scripts used during development.
- **`core/`**: Demonstrations of fundamental library features like animations and progress bars.
- **`results/`**: Standardized output directory for generated artifacts (e.g., HTML exports).

## 🎨 Visual Gallery

Coming soon... each directory will eventually include screenshots of the output.

## ⚖️ License

This project is licensed under the Apache 2.0 License.
