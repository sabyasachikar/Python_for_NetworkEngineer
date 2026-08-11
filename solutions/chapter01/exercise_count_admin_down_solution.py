"""
Solution to the Chapter 1 student exercise.
"""

interface_status = [
    {"device": "br-rtr-01", "interface": "Gig0/0", "admin": "up", "line": "up"},
    {"device": "br-rtr-01", "interface": "Gig0/1", "admin": "up", "line": "down"},
    {"device": "br-rtr-02", "interface": "Gig0/0", "admin": "up", "line": "up"},
    {"device": "br-rtr-02", "interface": "Gig0/1", "admin": "down", "line": "down"},
    {"device": "br-rtr-03", "interface": "Gig0/0", "admin": "up", "line": "down"},
]


def count_admin_down(records):
    """Count how many interfaces have an admin state of down."""
    total = 0
    for row in records:
        if row["admin"] == "down":
            total += 1
    return total


print(f"Interfaces shut on purpose: {count_admin_down(interface_status)}")
