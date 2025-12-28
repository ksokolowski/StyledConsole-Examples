# StyledConsole-Examples Makefile
# Runner for StyledConsole examples
# Requires: styledconsole package to be installed

.PHONY: help setup all auto list core frames gradients banners usecases validation fast check

# Detect UV or fall back to pip
UV := $(shell command -v uv 2> /dev/null)
ifdef UV
    INSTALL_CMD := uv pip install styledconsole
    SYNC_CMD := uv sync
else
    INSTALL_CMD := pip install styledconsole
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
	@echo "  make fast          Run all examples (skip validation)"
	@echo "  make list          List available categories"
	@echo ""
	@echo "Run by Category:"
	@echo "  make core          Run core feature examples"
	@echo "  make frames        Run frame system examples"
	@echo "  make gradients     Run gradient effect examples"
	@echo "  make banners       Run banner examples"
	@echo "  make usecases      Run use case examples"
	@echo "  make validation    Run validation examples"
	@echo ""
	@echo "Usage Tips:"
	@echo "  - Run 'make setup' first to install dependencies"
	@echo "  - Interactive mode pauses between examples"
	@echo "  - Auto mode runs continuously"
	@echo "  - Fast mode skips validation/testing examples"

# Setup
setup:
	@echo "📦 Installing StyledConsole..."
ifdef UV
	@echo "Using uv for installation..."
	@$(SYNC_CMD)
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
core:
	@python run_examples.py --categories core

frames:
	@python run_examples.py --categories frames

gradients:
	@python run_examples.py --categories gradients

banners:
	@python run_examples.py --categories banners

usecases:
	@python run_examples.py --categories usecases

validation:
	@python run_examples.py --categories validation
