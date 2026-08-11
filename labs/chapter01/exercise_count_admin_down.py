"""
Student exercise for Chapter 1.

The audit demo ignores interfaces that are administratively down, because those
were shut on purpose. Your network team now also wants a simple count of how many
interfaces were shut on purpose, so they can spot a router where too many ports
are disabled.

Task (complete this after Chapter 5):
    Write a function count_admin_down(records) that returns the number of
    interfaces whose admin state is "down".

Run your version and confirm it prints 1 for the sample data below.
"""

interface_status = [
    {"device": "br-rtr-01", "interface": "Gig0/0", "admin": "up", "line": "up"},
    {"device": "br-rtr-01", "interface": "Gig0/1", "admin": "up", "line": "down"},
    {"device": "br-rtr-02", "interface": "Gig0/0", "admin": "up", "line": "up"},
    {"device": "br-rtr-02", "interface": "Gig0/1", "admin": "down", "line": "down"},
    {"device": "br-rtr-03", "interface": "Gig0/0", "admin": "up", "line": "down"},
]


def count_admin_down(records):
    # TODO: return how many records have admin == "down"
    pass


print(f"Interfaces shut on purpose: {count_admin_down(interface_status)}")
