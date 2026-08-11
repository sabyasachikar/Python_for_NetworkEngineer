"""
Challenge lab for Chapter 1 (a little harder).

Instead of one flat list of problem interfaces, your team lead wants a per-device
summary, so at a glance they can see which router has the most trouble.

Task (complete this after Chapter 5):
    Write a function problems_by_device(records) that returns a dictionary where
    each key is a device name and each value is the list of that device's
    interfaces that are admin "up" but line "down".

    Then print a summary such as:
        br-rtr-01: 1 interface(s) down  -> Gig0/1
        br-rtr-03: 1 interface(s) down  -> Gig0/0

Devices with no problem interfaces should not appear in the summary.
"""

interface_status = [
    {"device": "br-rtr-01", "interface": "Gig0/0", "admin": "up", "line": "up"},
    {"device": "br-rtr-01", "interface": "Gig0/1", "admin": "up", "line": "down"},
    {"device": "br-rtr-02", "interface": "Gig0/0", "admin": "up", "line": "up"},
    {"device": "br-rtr-02", "interface": "Gig0/1", "admin": "down", "line": "down"},
    {"device": "br-rtr-03", "interface": "Gig0/0", "admin": "up", "line": "down"},
]


def problems_by_device(records):
    # TODO: build and return the dictionary described above
    pass


# TODO: loop over the result and print the summary lines
