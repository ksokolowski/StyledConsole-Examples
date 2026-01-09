"""
JSON Table Demo
==============

Demonstrates how to build a GradientTable entirely from configuration data,
simulating loading from a JSON file.
"""

from styledconsole import Console
from styledconsole.presets.tables import create_table_from_config
from styledconsole.policy import RenderPolicy

def run_demo():
    console = Console(policy=RenderPolicy(unicode=True, color=True))
    console.print("\n[bold]JSON Table Builder Demo[/bold]\n")

    # 1. Define Theme Configuration (Visuals)
    theme_config = {
        "title": "SERVER STATUS",
        "title_style": "bold italic white",
        "border_style": "heavy",
        "gradient": {
            "start": "chartreuse1",
            "end": "dodger_blue1",
            "direction": "horizontal"
        },
        "padding": (0, 2),
        "target": "border"
    }

    # 2. Define Data Configuration (Content)
    # Cells can be simple strings or objects with 'text', 'icon', 'color'
    data_config = {
        "columns": [
            {"header": "REGION", "style": "bold white", "justify": "left"},
            {"header": "CLUSTER", "style": "cyan", "justify": "left"},
            {"header": "STATUS", "style": "bold", "justify": "center"},
            {"header": "LATENCY", "style": "dim white", "justify": "right"}
        ],
        "rows": [
            [
                {"text": "US-East-1", "icon": "GLOBE_WITH_MERIDIANS"},
                "alpha-cluster-01",
                {"text": "ONLINE", "icon": "CHECK_MARK_BUTTON", "color": "green"},
                "24ms"
            ],
            [
                {"text": "EU-West-2", "icon": "GLOBE_WITH_MERIDIANS"},
                "bravo-cluster-09",
                {"text": "MAINTENANCE", "icon": "GEAR", "color": "yellow"},
                "89ms"
            ],
            [
                {"text": "AP-South-1", "icon": "GLOBE_WITH_MERIDIANS"},
                "delta-cluster-03",
                {"text": "OFFLINE", "icon": "CROSS_MARK", "color": "red"},
                "---"
            ]
        ]
    }

    # 3. Create and Print
    table = create_table_from_config(theme_config, data_config)
    console.print(table)
    
    console.print("\n[dim]Table generated from dictionary configuration.[/]\n")

if __name__ == "__main__":
    run_demo()
