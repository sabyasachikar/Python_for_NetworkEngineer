"""
interface_audit_demo.py

An OPTIONAL look-ahead script mentioned in Chapter 1.

You are not expected to understand this yet. It uses variables, lists,
dictionaries, a function, a loop, and an if statement, which are taught one at a
time across Chapters 2 to 5. Come back to it after Chapter 5 and every line will
make sense. It is here only to show, later on, how the ideas fit together in a
fuller program.

Once you have finished Chapter 5, run it with:

    python interface_audit_demo.py
"""

# A small piece of mock data that stands in for output you would normally
# collect from real devices. Each dictionary is one interface on one router.
# "admin" is the administrative state (did someone turn it on or off).
# "line"  is the actual line state (is it really passing traffic).
interface_status = [
    {"device": "br-rtr-01", "interface": "Gig0/0", "admin": "up", "line": "up"},
    {"device": "br-rtr-01", "interface": "Gig0/1", "admin": "up", "line": "down"},
    {"device": "br-rtr-02", "interface": "Gig0/0", "admin": "up", "line": "up"},
    {"device": "br-rtr-02", "interface": "Gig0/1", "admin": "down", "line": "down"},
    {"device": "br-rtr-03", "interface": "Gig0/0", "admin": "up", "line": "down"},
]


def find_down_links(records):
    """Return interfaces that are administratively up but the line is down.

    Those are the ones worth a human's attention. An interface that is
    administratively down was shut on purpose, so we leave it alone.
    """
    problems = []
    for row in records:
        if row["admin"] == "up" and row["line"] == "down":
            problems.append(row)
    return problems


down_links = find_down_links(interface_status)

print(f"Checked {len(interface_status)} interfaces across the branch routers.")
print(f"Found {len(down_links)} interface(s) that need attention:")
print()

for row in down_links:
    print(f"  {row['device']}  {row['interface']}  admin={row['admin']} line={row['line']}")
