# device_banner.py
# A small program that prints a tidy summary for one device.
# It uses only the things taught in Chapter 2: variables, text, numbers,
# booleans, and f-strings. No lists, loops, or functions yet.

# Store the facts about one device, each in its own variable.
hostname = "core-sw-01"          # text, so it is in quotes
mgmt_ip = "10.0.0.1"             # text as well, an address is not a number
vlan_count = 12                  # a whole number, no quotes
uplink_gbps = 10.0               # a decimal number
is_reachable = True              # a yes or no value

# Print a header.
print("Device summary")
print("==============")

# Print each fact on its own line. The f before the quotes lets us drop a
# variable straight into the text by putting its name in curly braces.
print(f"Hostname     : {hostname}")
print(f"Management IP: {mgmt_ip}")
print(f"VLAN count   : {vlan_count}")
print(f"Uplink speed : {uplink_gbps} Gbps")
print(f"Reachable    : {is_reachable}")
