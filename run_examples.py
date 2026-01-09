#!/usr/bin/env python3
"""
StyledConsole Examples Runner
==============================

A robust example runner that executes all StyledConsole examples in organized categories.

Features:
- Organized by numbered category (01-09)
- Interactive mode with pauses between examples
- Auto mode for continuous execution
- Category filtering (run specific categories only)
- Comprehensive error handling and reporting
- Progress tracking
- Summary statistics

Usage:
    # Run all examples interactively
    python run_examples.py

    # Run all examples without pauses
    python run_examples.py --auto

    # Run specific categories only
    python run_examples.py --categories 01_quickstart,04_effects

    # Run in fast mode (skip testing examples)
    python run_examples.py --fast

    # List available categories
    python run_examples.py --list
"""

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import List


def check_styledconsole_installed() -> bool:
    """Check if styledconsole is installed and importable."""
    try:
        import styledconsole
        return True
    except ImportError:
        return False


def print_installation_instructions() -> None:
    """Print helpful installation instructions for styledconsole."""
    print("\n" + "=" * 80)
    print("❌ ERROR: StyledConsole is not installed".center(80))
    print("=" * 80 + "\n")
    print("The examples require the 'styledconsole' package to be installed.\n")
    print("📦 Installation Options:\n")
    print("Option 1: Use the Makefile")
    print("  make setup")
    print()
    print("Option 2: Install manually")
    print("  uv pip install -e ../StyledConsole")
    print("  # or")
    print("  pip install -e ../StyledConsole")
    print()
    print("💡 After installation, run this script again to execute examples.")
    print("\n" + "=" * 80 + "\n")


@dataclass
class ExampleCategory:
    """Represents a category of examples."""
    name: str
    path: Path
    description: str
    icon: str
    priority: int  # Lower number = run first


@dataclass
class ExampleResult:
    """Result of running an example."""
    path: Path
    category: str
    success: bool
    duration: float
    error_message: str = ""


class ExamplesRunner:
    """Manages and executes StyledConsole examples."""

    def __init__(self, examples_root: Path, auto_mode: bool = False):
        """Initialize the examples runner."""
        self.examples_root = examples_root
        self.auto_mode = auto_mode
        self.results: List[ExampleResult] = []

        # Define categories with priority (lower = run first)
        self.categories = [
            ExampleCategory(
                name="01_quickstart",
                path=examples_root / "01_quickstart",
                description="Getting Started - First steps with StyledConsole",
                icon="🚀",
                priority=1,
            ),
            ExampleCategory(
                name="02_frames",
                path=examples_root / "02_frames",
                description="Frame System - Borders, Nesting, Margins, Styles",
                icon="🖼️",
                priority=2,
            ),
            ExampleCategory(
                name="03_content",
                path=examples_root / "03_content",
                description="Content Elements - Tables, Text, Rules",
                icon="📝",
                priority=3,
            ),
            ExampleCategory(
                name="04_effects",
                path=examples_root / "04_effects",
                description="Visual Effects - Gradients, Palettes, Animation",
                icon="🌈",
                priority=4,
            ),
            ExampleCategory(
                name="05_banners",
                path=examples_root / "05_banners",
                description="ASCII Art Banners - Welcome Screens, Dashboards",
                icon="🔤",
                priority=5,
            ),
            ExampleCategory(
                name="06_advanced",
                path=examples_root / "06_advanced",
                description="Advanced Features - Policies, JSON Layouts",
                icon="⚙️",
                priority=6,
            ),
            ExampleCategory(
                name="07_showcases",
                path=examples_root / "07_showcases",
                description="Feature Showcases - Icons, Emoji, Progress",
                icon="✨",
                priority=7,
            ),
            ExampleCategory(
                name="08_applications",
                path=examples_root / "08_applications",
                description="Real-World Applications - CLI Menus, Logs, Alerts",
                icon="💼",
                priority=8,
            ),
            ExampleCategory(
                name="09_testing",
                path=examples_root / "09_testing",
                description="Testing & Validation - Benchmarks, Compatibility",
                icon="🧪",
                priority=9,
            ),
        ]

    def list_categories(self) -> None:
        """Print available categories."""
        print("\n" + "=" * 80)
        print("📚 Available Example Categories".center(80))
        print("=" * 80 + "\n")

        for category in sorted(self.categories, key=lambda c: c.priority):
            example_files = self._get_example_files(category)
            count = len(example_files)
            exists = "✅" if category.path.exists() else "❌"

            print(f"{category.icon}  {category.name}")
            print(f"   {category.description}")
            print(f"   Examples: {count} {exists}")
            print()

        print("=" * 80 + "\n")

    def run_all(self, selected_categories: List[str] = None, skip_testing: bool = False) -> None:
        """Run all examples in sequence."""
        # Filter categories
        categories_to_run = []
        for category in sorted(self.categories, key=lambda c: c.priority):
            if selected_categories and category.name not in selected_categories:
                continue
            if skip_testing and category.name == "09_testing":
                continue
            if not category.path.exists():
                print(f"⚠️  Warning: Category '{category.name}' not found")
                continue
            categories_to_run.append(category)

        if not categories_to_run:
            print("❌ No valid categories selected or found.")
            return

        # Print header
        self._print_header(categories_to_run)

        if not self.auto_mode:
            input("\n👉 Press Enter to start running examples...")

        # Run each category
        total_start_time = time.time()

        for i, category in enumerate(categories_to_run, 1):
            self._run_category(category, i, len(categories_to_run))

        total_duration = time.time() - total_start_time

        # Print summary
        self._print_summary(total_duration)

    def _print_header(self, categories: List[ExampleCategory]) -> None:
        """Print the runner header."""
        print("\n" + "=" * 80)
        print("✨ STYLEDCONSOLE EXAMPLES SHOWCASE ✨".center(80))
        print("=" * 80)
        print()
        print("This will run all examples in organized categories for visual inspection.")
        mode = "AUTO MODE (no pauses)" if self.auto_mode else "INTERACTIVE MODE (press Enter between examples)"
        print(f"Mode: {mode}")
        print()
        print("Categories to run:")
        for category in categories:
            example_files = self._get_example_files(category)
            print(f"  {category.icon} {category.name}: {len(example_files)} examples")
        print()

    def _run_category(self, category: ExampleCategory, category_num: int, total_categories: int) -> None:
        """Run all examples in a category."""
        example_files = self._get_example_files(category)

        if not example_files:
            print(f"\n⚠️  No examples found in category '{category.name}'")
            return

        # Print category header
        print("\n" + "=" * 80)
        print(f"{category.icon}  CATEGORY {category_num}/{total_categories}: {category.name}".center(80))
        print("=" * 80)
        print(f"{category.description}".center(80))
        print("=" * 80 + "\n")

        # Run each example
        for i, example_path in enumerate(example_files, 1):
            self._run_example(example_path, category.name, i, len(example_files))

    def _run_example(
        self, example_path: Path, category: str, example_num: int, total_examples: int
    ) -> None:
        """Run a single example file."""
        print(f"\n📝 [{example_num}/{total_examples}] {category}/{example_path.name}")
        print("-" * 80)

        start_time = time.time()
        success = False
        error_message = ""

        try:
            # Find the main StyledConsole repository
            main_repo = self.examples_root.parent / "StyledConsole"

            if main_repo.exists() and (main_repo / "pyproject.toml").exists():
                # Use uv run from the main repository context
                result = subprocess.run(
                    ["uv", "run", "python", str(example_path)],
                    capture_output=False,
                    text=True,
                    check=True,
                    cwd=main_repo,
                )
            else:
                # Fallback to regular python execution
                result = subprocess.run(
                    [sys.executable, str(example_path)],
                    capture_output=False,
                    text=True,
                    check=True,
                    cwd=example_path.parent,
                )

            duration = time.time() - start_time
            success = True

            print("-" * 80)
            print(f"✅ Completed: {example_path.name} ({duration:.2f}s)")

        except subprocess.CalledProcessError as e:
            duration = time.time() - start_time
            error_message = f"Exit code: {e.returncode}"

            print("-" * 80)
            print(f"❌ Error running {example_path.name}")
            print(f"   {error_message}")

        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted by user")
            self._print_summary(time.time() - start_time, interrupted=True)
            sys.exit(0)

        except Exception as e:
            duration = time.time() - start_time
            error_message = str(e)

            print("-" * 80)
            print(f"❌ Unexpected error: {error_message}")

        # Record result
        self.results.append(
            ExampleResult(
                path=example_path,
                category=category,
                success=success,
                duration=duration,
                error_message=error_message,
            )
        )

        # Pause if interactive mode
        if not self.auto_mode and success:
            try:
                input("\n👉 Press Enter to continue to next example...")
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted by user")
                self._print_summary(time.time() - start_time, interrupted=True)
                sys.exit(0)
        elif not success and not self.auto_mode:
            try:
                response = input("\n⚠️  Continue anyway? (y/n): ")
                if response.lower() != "y":
                    print("\nExiting...")
                    sys.exit(1)
            except KeyboardInterrupt:
                print("\n\n⚠️  Interrupted by user")
                sys.exit(0)

    def _get_example_files(self, category: ExampleCategory) -> List[Path]:
        """Get all example files in a category."""
        if not category.path.exists():
            return []

        # Get all .py files, excluding __init__.py and files starting with _
        files = [
            f
            for f in category.path.glob("*.py")
            if f.name != "__init__.py" and not f.name.startswith("_")
        ]

        return sorted(files)

    def _print_summary(self, total_duration: float, interrupted: bool = False) -> None:
        """Print execution summary."""
        print("\n" + "=" * 80)
        print("📊 EXECUTION SUMMARY".center(80))
        print("=" * 80 + "\n")

        if interrupted:
            print("⚠️  Execution was interrupted\n")

        # Count results
        successful = sum(1 for r in self.results if r.success)
        failed = sum(1 for r in self.results if not r.success)
        total = len(self.results)

        print(f"Total examples run: {total}")
        print(f"Successful: {successful} ✅")
        print(f"Failed: {failed} ❌")
        print(f"Total duration: {total_duration:.2f}s")
        print()

        # Print failures if any
        if failed > 0:
            print("Failed examples:")
            for result in self.results:
                if not result.success:
                    print(f"  ❌ {result.category}/{result.path.name}")
                    if result.error_message:
                        print(f"     {result.error_message}")
            print()

        print("=" * 80 + "\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Run StyledConsole examples",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--auto",
        action="store_true",
        help="Run without pauses between examples",
    )

    parser.add_argument(
        "--categories",
        type=str,
        help="Comma-separated list of categories to run (e.g., 01_quickstart,04_effects)",
    )

    parser.add_argument(
        "--fast",
        action="store_true",
        help="Skip testing examples (09_testing)",
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="List available categories and exit",
    )

    args = parser.parse_args()

    # Determine examples root directory
    examples_root = Path(__file__).parent

    # Create runner
    runner = ExamplesRunner(examples_root, auto_mode=args.auto)

    # List categories if requested
    if args.list:
        runner.list_categories()
        return

    # Check if styledconsole is installed
    if not check_styledconsole_installed():
        print_installation_instructions()
        sys.exit(1)

    # Parse categories if provided
    selected_categories = None
    if args.categories:
        selected_categories = [c.strip() for c in args.categories.split(",")]

    # Run examples
    runner.run_all(
        selected_categories=selected_categories,
        skip_testing=args.fast,
    )


if __name__ == "__main__":
    main()
