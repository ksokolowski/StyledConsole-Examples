#!/usr/bin/env python3
"""Hello Frame - Your first StyledConsole example.

This is the simplest possible StyledConsole example.
Run this to verify your installation works!

Usage:
    python 01_quickstart/hello_frame.py
"""

from styledconsole import Console

# Create a console instance
console = Console()

# Display a simple frame
console.frame("Hello, StyledConsole!", title="Welcome")
