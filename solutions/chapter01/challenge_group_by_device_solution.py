"""
Solution to the Chapter 1 challenge lab.
"""

interface_status = [
    {"device": "br-rtr-01", "interface": "Gig0/0", "admin": "up", "line": "up"},
    {"device": "br-rtr-01", "interface": "Gig0/1", "admin": "up", "line": "down"},
    {"device": "br-rtr-02", "interface": "Gig0/0", "admin": "up", "line": "up"},
    {"device": "br-rtr-02", "interface": "Gig0/1", "admin": "down", "line": "down"},
    {"device": "br-rtr-03", "interface": "Gig0/0", "admin": "up", "line": "down"},
]


def problems_by_device(records):
    """Group problem interfaces (admin up, line down) by device name."""
    grouped = {}
    for row in records:
        if row["admin"] == "up" and row["line"] == "down":
            device = row["device"]
            if device not in grouped:
                grouped[device] = []
            grouped[device].append(row["interface"])
    return grouped


summary = problems_by_device(interface_status)

for device, interfaces in summary.items():
    joined = ", ".join(interfaces)
    print(f"{device}: {len(interfaces)} interface(s) down  -> {joined}")
