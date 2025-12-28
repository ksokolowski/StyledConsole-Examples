#!/usr/bin/env python3
"""
StyledConsole Examples Runner
==============================

A robust example runner that executes all StyledConsole examples in organized categories.

Features:
- Organized by category (core, frames, gradients, banners, usecases, validation)
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
    python run_examples.py --categories core,frames

    # Run in fast mode (skip validation examples)
    python run_examples.py --fast

    # List available categories
    python run_examples.py --list

Examples:
    # Interactive mode (default)
    python run_examples.py

    # Auto mode
    python run_examples.py --auto

    # Run only core and usecases
    python run_examples.py --categories core,usecases --auto
"""

import argparse
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import List


def check_styledconsole_installed() -> bool:
    """Check if styledconsole is installed and importable.

    Returns:
        True if styledconsole is available, False otherwise
    """
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

    print("Option 1: Install using pip")
    print("  pip install styledconsole")
    print()

    print("Option 2: Install using uv (recommended for development)")
    print("  uv pip install styledconsole")
    print()

    print("Option 3: Install from this repository's dependencies")
    print("  uv sync")
    print("  # or")
    print("  pip install -e .")
    print()

    print("Option 4: Use the Makefile")
    print("  make setup")
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
        """Initialize the examples runner.

        Args:
            examples_root: Root directory containing example categories
            auto_mode: If True, run without pauses between examples
        """
        self.examples_root = examples_root
        self.auto_mode = auto_mode
        self.results: List[ExampleResult] = []

        # Define categories with priority (lower = run first)
        self.categories = [
            ExampleCategory(
                name="core",
                path=examples_root / "core",
                description="Core Features - Icon Provider, Render Policy, Animation, Progress",
                icon="⚙️",
                priority=1,
            ),
            ExampleCategory(
                name="frames",
                path=examples_root / "frames",
                description="Frame System - Borders, Nesting, Margins, Styles",
                icon="🖼️",
                priority=2,
            ),
            ExampleCategory(
                name="gradients",
                path=examples_root / "gradients",
                description="Gradient Effects - Rainbow, Nested, Animated",
                icon="🌈",
                priority=3,
            ),
            ExampleCategory(
                name="banners",
                path=examples_root / "banners",
                description="ASCII Art Banners - Welcome Screens, Dashboards",
                icon="🔤",
                priority=4,
            ),
            ExampleCategory(
                name="usecases",
                path=examples_root / "usecases",
                description="Real-World Use Cases - CLI Menus, Logs, Alerts, Tables",
                icon="💼",
                priority=5,
            ),
            ExampleCategory(
                name="validation",
                path=examples_root / "validation",
                description="Validation & Testing - Terminal Compatibility, Benchmarks",
                icon="🧪",
                priority=6,
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

            print(f"{category.icon}  {category.name.upper()}")
            print(f"   {category.description}")
            print(f"   Examples: {count}")
            print()

        print("=" * 80 + "\n")

    def run_all(self, selected_categories: List[str] = None, skip_validation: bool = False) -> None:
        """Run all examples in sequence.

        Args:
            selected_categories: List of category names to run. If None, run all.
            skip_validation: If True, skip validation category
        """
        # Filter categories
        categories_to_run = []
        for category in sorted(self.categories, key=lambda c: c.priority):
            if selected_categories and category.name not in selected_categories:
                continue
            if skip_validation and category.name == "validation":
                continue
            if not category.path.exists():
                print(f"⚠️  Warning: Category '{category.name}' not found at {category.path}")
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
            print(f"  {category.icon} {category.name.title()}: {len(example_files)} examples")
        print()

    def _run_category(self, category: ExampleCategory, category_num: int, total_categories: int) -> None:
        """Run all examples in a category.

        Args:
            category: Category to run
            category_num: Current category number
            total_categories: Total number of categories
        """
        example_files = self._get_example_files(category)

        if not example_files:
            print(f"\n⚠️  No examples found in category '{category.name}'")
            return

        # Print category header
        print("\n" + "=" * 80)
        print(f"{category.icon}  CATEGORY {category_num}/{total_categories}: {category.name.upper()}".center(80))
        print("=" * 80)
        print(f"{category.description}".center(80))
        print("=" * 80 + "\n")

        # Run each example
        for i, example_path in enumerate(example_files, 1):
            self._run_example(example_path, category.name, i, len(example_files))

    def _run_example(
        self, example_path: Path, category: str, example_num: int, total_examples: int
    ) -> None:
        """Run a single example file.

        Args:
            example_path: Path to the example file
            category: Category name
            example_num: Current example number within category
            total_examples: Total examples in category
        """
        print(f"\n📝 [{example_num}/{total_examples}] {category}/{example_path.name}")
        print("-" * 80)

        start_time = time.time()
        success = False
        error_message = ""

        try:
            # Find the main StyledConsole repository (one level up from Examples repo)
            main_repo = self.examples_root.parent / "StyledConsole"

            # Run the example using uv run from the main repository if it exists
            if main_repo.exists() and (main_repo / "pyproject.toml").exists():
                # Use uv run from the main repository context
                result = subprocess.run(
                    ["uv", "run", "python", str(example_path)],
                    capture_output=False,
                    text=True,
                    check=True,
                    cwd=main_repo,  # Run from main repo to access installed package
                )
            else:
                # Fallback to regular python execution (for standalone Examples repo)
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
        """Get all example files in a category.

        Args:
            category: Category to get files from

        Returns:
            Sorted list of example file paths
        """
        if not category.path.exists():
            return []

        # Get all .py files, excluding __init__.py and test files starting with test_
        files = [
            f
            for f in category.path.glob("*.py")
            if f.name != "__init__.py" and not f.name.startswith("_")
        ]

        return sorted(files)

    def _print_summary(self, total_duration: float, interrupted: bool = False) -> None:
        """Print execution summary.

        Args:
            total_duration: Total execution time in seconds
            interrupted: Whether execution was interrupted
        """
        print("\n" + "=" * 80)
        if interrupted:
            print("⚠️  EXAMPLES RUNNER INTERRUPTED".center(80))
        else:
            print("🎉 EXAMPLES SHOWCASE COMPLETED".center(80))
        print("=" * 80 + "\n")

        # Statistics
        total = len(self.results)
        successful = sum(1 for r in self.results if r.success)
        failed = total - successful

        print(f"📊 Statistics:")
        print(f"   Total examples run: {total}")
        print(f"   Successful: {successful} ✅")
        print(f"   Failed: {failed} ❌")
        print(f"   Total duration: {total_duration:.2f}s")

        if total > 0:
            avg_duration = sum(r.duration for r in self.results) / total
            print(f"   Average duration: {avg_duration:.2f}s")

        # Category breakdown
        if self.results:
            print(f"\n📁 By Category:")
            categories_seen = {}
            for result in self.results:
                if result.category not in categories_seen:
                    categories_seen[result.category] = {"total": 0, "success": 0}
                categories_seen[result.category]["total"] += 1
                if result.success:
                    categories_seen[result.category]["success"] += 1

            for category, stats in sorted(categories_seen.items()):
                icon = next((c.icon for c in self.categories if c.name == category), "📂")
                status = "✅" if stats["success"] == stats["total"] else "⚠️"
                print(
                    f"   {icon} {category.title()}: {stats['success']}/{stats['total']} {status}"
                )

        # Failed examples detail
        if failed > 0:
            print(f"\n❌ Failed Examples:")
            for result in self.results:
                if not result.success:
                    print(f"   - {result.category}/{result.path.name}")
                    if result.error_message:
                        print(f"     Error: {result.error_message}")

        print("\n" + "=" * 80 + "\n")


def main():
    """Main entry point."""
    # Check if styledconsole is installed (unless just listing)
    # Skip check if we can find the main StyledConsole repository with uv
    if "--list" not in sys.argv and "-l" not in sys.argv:
        examples_root = Path(__file__).parent
        main_repo = examples_root.parent / "StyledConsole"
        has_main_repo = main_repo.exists() and (main_repo / "pyproject.toml").exists()

        if not has_main_repo and not check_styledconsole_installed():
            print_installation_instructions()
            sys.exit(1)

    parser = argparse.ArgumentParser(
        description="StyledConsole Examples Runner - Execute examples in organized categories",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                 # Run all examples interactively
  %(prog)s --auto                          # Run all examples without pauses
  %(prog)s --categories core,frames        # Run only core and frames
  %(prog)s --fast                          # Skip validation examples
  %(prog)s --list                          # List available categories
        """,
    )

    parser.add_argument(
        "--auto",
        "-a",
        action="store_true",
        help="Auto mode: run without pauses between examples",
    )

    parser.add_argument(
        "--categories",
        "-c",
        type=str,
        help="Comma-separated list of categories to run (e.g., 'core,frames,usecases')",
    )

    parser.add_argument(
        "--fast",
        "-f",
        action="store_true",
        help="Fast mode: skip validation examples",
    )

    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List available categories and exit",
    )

    args = parser.parse_args()

    # Determine examples root
    examples_root = Path(__file__).parent.resolve()

    # Create runner
    runner = ExamplesRunner(examples_root, auto_mode=args.auto)

    # List mode
    if args.list:
        runner.list_categories()
        return

    # Parse categories
    selected_categories = None
    if args.categories:
        selected_categories = [c.strip() for c in args.categories.split(",")]

    # Run examples
    try:
        runner.run_all(selected_categories=selected_categories, skip_validation=args.fast)
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(0)


if __name__ == "__main__":
    main()
