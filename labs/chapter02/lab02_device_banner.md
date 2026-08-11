# Lab 2.1: Build a Device Banner

Write your first useful script from scratch. It uses only Chapter 2 material:
variables, the four value types, and f-strings.

## Objective

Print a clean, labeled summary of one device's key facts.

## Network scenario

You want a quick, repeatable way to print a device's key facts, the kind of thing you
will later generate for every device in your network.

## Prerequisites

Chapter 0 finished, so Python and your virtual environment are ready. Activate the
environment before you start.

## Files required

None to start. You create `scripts/chapter02/device_banner.py`.

## Steps

1. Create the file `scripts/chapter02/device_banner.py`.
2. Create five variables for one device:
   - `hostname` and `mgmt_ip` as text (in quotes)
   - `vlan_count` as an integer
   - `uplink_gbps` as a float
   - `is_reachable` as a boolean (`True` or `False`)
3. Print a two line header, for example `Device summary` and a line of `=` signs.
4. Print each fact on its own line with an f-string, keeping the labels aligned.
5. Save and run: `python scripts/chapter02/device_banner.py`.

## Expected output

```
Device summary
==============
Hostname     : core-sw-01
Management IP: 10.0.0.1
VLAN count   : 12
Uplink speed : 10.0 Gbps
Reachable    : True
```

## Verification

Your output matches and each value sits after its label. If a number printed with
quotes, you stored it as text by mistake.

## Common errors

- `NameError`: a variable was used before it was created, or the name is misspelled.
- The IP address raises an error: keep it in quotes, it is text.
- A line prints `{hostname}` literally: you forgot the `f` before the quotes.

## Student exercise

Make a banner for a second, different device: a different hostname and address, a
different VLAN count and speed, and `is_reachable = False`. Solution in
`solutions/chapter02/device_banner_edge_solution.py`.

## Challenge lab

The access and uplink port counts arrive as text, `"24"` and `"2"`. Convert both to
integers, add them, and print the total. In a comment, explain what `"24" + "2"`
would print instead and why. Solution in
`solutions/chapter02/challenge_port_count_solution.py`.
