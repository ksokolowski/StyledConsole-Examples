# StyledConsole-Examples Makefile
# Runner for StyledConsole examples
# Requires: styledconsole package to be installed

.PHONY: help setup all auto list quickstart frames content effects banners advanced showcases applications testing check

# Detect UV or fall back to pip
UV := $(shell command -v uv 2> /dev/null)
ifdef UV
    INSTALL_CMD := uv pip install -e ../StyledConsole
    SYNC_CMD := uv sync
else
    INSTALL_CMD := pip install -e ../StyledConsole
    SYNC_CMD := pip install -e .
endif

# Default target
help:
@echo "🎨 StyledConsole Examples Runner"
@echo "================================"
@echo "Setup:"
@echo "  make setup         Install styledconsole dependency"
@echo "  make check         Check if styledconsole is installed"
@echo ""
@echo "Run Examples:"
@echo "  make all           Run all examples (interactive)"
@echo "  make auto          Run all examples (auto mode)"
@echo "  make fast          Run all examples (skip testing)"
@echo "  make list          List available categories"
@echo ""
@echo "Run by Category:"
@echo "  make quickstart    Run 01_quickstart examples"
@echo "  make frames        Run 02_frames examples"
@echo "  make content       Run 03_content examples"
@echo "  make effects       Run 04_effects examples"
@echo "  make banners       Run 05_banners examples"
@echo "  make advanced      Run 06_advanced examples"
@echo "  make showcases     Run 07_showcases examples"
@echo "  make applications  Run 08_applications examples"
@echo "  make testing       Run 09_testing examples"
@echo ""
@echo "Usage Tips:"
@echo "  - Run 'make setup' first to install dependencies"
@echo "  - Interactive mode pauses between examples"
@echo "  - Auto mode runs continuously"
@echo "  - Fast mode skips testing examples"

# Setup
setup:
@echo "📦 Installing StyledConsole..."
ifdef UV
@echo "Using uv for installation..."
@$(INSTALL_CMD)
else
@echo "Using pip for installation..."
@$(INSTALL_CMD)
endif
@echo "✅ Setup complete! You can now run examples."

check:
@echo "🔍 Checking if styledconsole is installed..."
@python -c "import styledconsole; print('✅ styledconsole', styledconsole.__version__, 'is installed')" 2>/dev/null || \
(echo "❌ styledconsole is not installed. Run 'make setup' to install it." && exit 1)

# Run all examples
all:
@python run_examples.py

auto:
@python run_examples.py --auto

fast:
@python run_examples.py --fast

list:
@python run_examples.py --list

# Run specific categories
quickstart:
@python run_examples.py --categories 01_quickstart

frames:
@python run_examples.py --categories 02_frames

content:
@python run_examples.py --categories 03_content

effects:
@python run_examples.py --categories 04_effects

banners:
@python run_examples.py --categories 05_banners

advanced:
@python run_examples.py --categories 06_advanced

showcases:
@python run_examples.py --categories 07_showcases

applications:
@python run_examples.py --categories 08_applications

testing:
@python run_examples.py --categories 09_testing
