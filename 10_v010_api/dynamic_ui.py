#!/usr/bin/env python3
"""Dynamic UI Generation Example - v0.10.0 Declarative API.

Demonstrates generating UI dynamically from data sources like:
- API responses
- Database records
- User preferences
- Runtime configuration

Usage:
    python 10_v010_api/dynamic_ui.py
"""

from styledconsole import Console, icons, load_dict

console = Console()

console.text("[bold cyan]Dynamic UI Generation - v0.10.0 API[/]")
console.text("[dim]Build UI from data at runtime[/]")
console.newline()

# =============================================================================
# 1. Generate UI from API Response
# =============================================================================

console.rule("[yellow]1. UI from API Response[/]")
console.newline()


def simulate_api_response():
    """Simulate an API response with user data."""
    return {
        "user": {
            "name": "John Doe",
            "role": "Admin",
            "email": "john@example.com",
            "last_login": "2024-01-15 10:30",
        },
        "permissions": ["read", "write", "delete", "admin"],
        "notifications": [
            {"type": "info", "message": "Welcome back!"},
            {"type": "warning", "message": "Password expires in 5 days"},
        ],
    }


def build_user_card(api_data: dict) -> dict:
    """Build a user card UI from API data."""
    user = api_data["user"]
    perms = api_data["permissions"]

    # Build permissions list dynamically
    perm_icons = {
        "read": icons.MAG,
        "write": icons.MEMO,
        "delete": icons.WASTEBASKET,
        "admin": icons.KEY,
    }
    perm_lines = [f"  {perm_icons.get(p, icons.CHECK_MARK_BUTTON)} {p}" for p in perms]

    # Build notifications dynamically
    notif_lines = []
    for n in api_data["notifications"]:
        icon = icons.WARNING if n["type"] == "warning" else icons.BELL
        notif_lines.append(f"{icon} {n['message']}")

    return {
        "type": "layout",
        "direction": "vertical",
        "gap": 1,
        "children": [
            # User info frame
            {
                "frame": f"{icons.PERSON} {user['name']}\n{icons.STAR} {user['role']}\n{icons.E_MAIL} {user['email']}\n{icons.ALARM_CLOCK} Last login: {user['last_login']}",
                "title": "User Profile",
                "effect": "ocean",
            },
            # Permissions frame
            {
                "frame": "Permissions:\n" + "\n".join(perm_lines),
                "title": "Access Rights",
                "effect": "steel",
            },
            # Notifications
            {
                "frame": "\n".join(notif_lines) if notif_lines else "No notifications",
                "title": f"Notifications ({len(notif_lines)})",
                "effect": "sunset" if any(n["type"] == "warning" for n in api_data["notifications"]) else "ocean",
            },
        ],
    }


# Generate and render
api_data = simulate_api_response()
user_card = build_user_card(api_data)
console.render_dict(user_card)
console.newline()

# =============================================================================
# 2. Generate Table from Database Records
# =============================================================================

console.rule("[yellow]2. Table from Database Records[/]")
console.newline()


def simulate_db_query():
    """Simulate database query results."""
    return [
        {"id": 1, "name": "api-server", "status": "running", "cpu": 23, "memory": 512},
        {"id": 2, "name": "web-frontend", "status": "running", "cpu": 15, "memory": 256},
        {"id": 3, "name": "background-worker", "status": "stopped", "cpu": 0, "memory": 0},
        {"id": 4, "name": "cache-server", "status": "running", "cpu": 8, "memory": 1024},
        {"id": 5, "name": "db-replica", "status": "degraded", "cpu": 89, "memory": 2048},
    ]


def build_table_from_records(records: list) -> dict:
    """Build a table UI from database records."""
    # Build rows dynamically
    rows = []
    for r in records:
        # Status with icon
        if r["status"] == "running":
            status = f"{icons.CHECK_MARK_BUTTON} running"
        elif r["status"] == "degraded":
            status = f"{icons.WARNING} degraded"
        else:
            status = f"{icons.CROSS_MARK} stopped"

        # CPU with color coding
        if r["cpu"] > 80:
            cpu = f"[red]{r['cpu']}%[/]"
        elif r["cpu"] > 50:
            cpu = f"[yellow]{r['cpu']}%[/]"
        else:
            cpu = f"[green]{r['cpu']}%[/]"

        rows.append(f"  {r['id']:2}  {r['name']:<20}  {status:<15}  {cpu:<10}  {r['memory']} MB")

    header = f"  {'ID':2}  {'Name':<20}  {'Status':<15}  {'CPU':<10}  Memory"
    separator = "  " + "-" * 65

    content = "\n".join([header, separator] + rows)

    return {
        "frame": content,
        "title": f"Processes ({len(records)} total)",
        "effect": "steel",
        "border": "rounded",
    }


records = simulate_db_query()
table_ui = build_table_from_records(records)
console.render_dict(table_ui)
console.newline()

# =============================================================================
# 3. Generate Form from Schema
# =============================================================================

console.rule("[yellow]3. Form UI from Schema[/]")
console.newline()


def get_form_schema():
    """Simulate a form schema (like JSON Schema)."""
    return {
        "title": "User Registration",
        "fields": [
            {"name": "username", "type": "text", "required": True, "label": "Username"},
            {"name": "email", "type": "email", "required": True, "label": "Email"},
            {"name": "password", "type": "password", "required": True, "label": "Password"},
            {"name": "role", "type": "select", "options": ["user", "admin", "moderator"], "label": "Role"},
            {"name": "newsletter", "type": "checkbox", "label": "Subscribe to newsletter"},
        ],
    }


def build_form_preview(schema: dict) -> dict:
    """Build a form preview UI from schema."""
    field_icons = {
        "text": icons.MEMO,
        "email": icons.E_MAIL,
        "password": icons.KEY,
        "select": icons.ARROW_DOWN,
        "checkbox": icons.CHECK_MARK_BUTTON,
    }

    lines = []
    for field in schema["fields"]:
        icon = field_icons.get(field["type"], icons.GEAR)
        required = "[red]*[/]" if field.get("required") else " "
        type_hint = f"[dim]({field['type']})[/]"

        if field["type"] == "select":
            options = ", ".join(field.get("options", []))
            lines.append(f"{icon} {field['label']}{required} {type_hint}")
            lines.append(f"   [dim]Options: {options}[/]")
        else:
            lines.append(f"{icon} {field['label']}{required} {type_hint}")

    return {
        "frame": "\n".join(lines),
        "title": schema["title"],
        "subtitle": f"{len(schema['fields'])} fields",
        "effect": "ocean",
    }


schema = get_form_schema()
form_ui = build_form_preview(schema)
console.render_dict(form_ui)
console.newline()

# =============================================================================
# 4. Generate Navigation from Route Config
# =============================================================================

console.rule("[yellow]4. Navigation from Routes[/]")
console.newline()


def get_route_config():
    """Simulate route configuration."""
    return [
        {"path": "/", "name": "Home", "icon": "home"},
        {"path": "/dashboard", "name": "Dashboard", "icon": "chart"},
        {"path": "/users", "name": "Users", "icon": "users", "children": [
            {"path": "/users/list", "name": "User List"},
            {"path": "/users/add", "name": "Add User"},
        ]},
        {"path": "/settings", "name": "Settings", "icon": "gear"},
        {"path": "/help", "name": "Help", "icon": "help"},
    ]


def build_nav_menu(routes: list, current: str = "/dashboard") -> dict:
    """Build navigation menu from routes."""
    nav_icons = {
        "home": icons.HOME,
        "chart": icons.CHART_INCREASING,
        "users": icons.BUSTS_IN_SILHOUETTE,
        "gear": icons.GEAR,
        "help": icons.RED_QUESTION_MARK,
    }

    lines = []
    for route in routes:
        icon = nav_icons.get(route.get("icon", ""), icons.ARROW_RIGHT)
        is_active = route["path"] == current

        if is_active:
            lines.append(f"[bold cyan]{icon} {route['name']}[/] [dim]<--[/]")
        else:
            lines.append(f"{icon} {route['name']}")

        # Render children
        for child in route.get("children", []):
            prefix = "   " if not is_active else "   "
            lines.append(f"{prefix}{icons.ARROW_RIGHT} {child['name']}")

    return {
        "frame": "\n".join(lines),
        "title": "Navigation",
        "effect": "steel",
        "border": "rounded",
    }


routes = get_route_config()
nav_ui = build_nav_menu(routes, current="/dashboard")
console.render_dict(nav_ui)
console.newline()

# =============================================================================
# 5. Generate Report from Analytics Data
# =============================================================================

console.rule("[yellow]5. Report from Analytics[/]")
console.newline()


def get_analytics_data():
    """Simulate analytics data."""
    return {
        "period": "Last 7 days",
        "summary": {
            "total_users": 12543,
            "active_users": 8234,
            "new_signups": 523,
            "revenue": 45230.50,
        },
        "top_pages": [
            {"path": "/home", "views": 45234},
            {"path": "/products", "views": 23456},
            {"path": "/checkout", "views": 12345},
        ],
        "trends": {"users": "+12%", "revenue": "+8%", "engagement": "-2%"},
    }


def build_analytics_report(data: dict) -> dict:
    """Build analytics report UI."""
    summary = data["summary"]
    trends = data["trends"]

    # Format trend indicators
    def trend_icon(t):
        if t.startswith("+"):
            return f"[green]{icons.ARROW_UP} {t}[/]"
        elif t.startswith("-"):
            return f"[red]{icons.ARROW_DOWN} {t}[/]"
        return t

    summary_lines = [
        f"{icons.BUSTS_IN_SILHOUETTE} Total Users: {summary['total_users']:,}",
        f"{icons.PERSON} Active Users: {summary['active_users']:,} {trend_icon(trends['users'])}",
        f"{icons.SPARKLES} New Signups: {summary['new_signups']:,}",
        f"{icons.MONEY_BAG} Revenue: ${summary['revenue']:,.2f} {trend_icon(trends['revenue'])}",
    ]

    top_pages_lines = [f"{icons.CHART_INCREASING} Top Pages:"]
    for i, page in enumerate(data["top_pages"], 1):
        top_pages_lines.append(f"   {i}. {page['path']} - {page['views']:,} views")

    return {
        "type": "layout",
        "direction": "vertical",
        "gap": 1,
        "children": [
            {
                "banner": "ANALYTICS",
                "font": "small",
                "effect": "ocean",
            },
            {
                "frame": f"[dim]Period: {data['period']}[/]\n\n" + "\n".join(summary_lines),
                "title": "Summary",
                "effect": "steel",
            },
            {
                "frame": "\n".join(top_pages_lines),
                "title": "Traffic",
                "effect": "ocean",
            },
        ],
    }


analytics = get_analytics_data()
report_ui = build_analytics_report(analytics)
console.render_dict(report_ui)
console.newline()

# =============================================================================
# Summary
# =============================================================================

console.frame(
    f"""
[bold cyan]Dynamic UI Generation Benefits:[/]

{icons.SPARKLES} Build UI directly from API responses
{icons.SPARKLES} Generate tables from database queries
{icons.SPARKLES} Create forms from JSON schemas
{icons.SPARKLES} Construct menus from route configs
{icons.SPARKLES} Render reports from analytics data
{icons.SPARKLES} Full runtime customization
    """.strip(),
    border="rounded_thick",
    border_color="lime",
    padding=1,
)
