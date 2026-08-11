# challenge_port_count_solution.py
# Solution to the Chapter 2 challenge.
#
# The port counts arrive as text (imagine they came from a form or a file).
# Text cannot be added like numbers, so we convert each one to an integer
# with int() first, then add them.

access_ports_text = "24"
uplink_ports_text = "2"

access_ports = int(access_ports_text)   # "24" becomes 24
uplink_ports = int(uplink_ports_text)   # "2"  becomes 2

total_ports = access_ports + uplink_ports

print(f"Access ports : {access_ports}")
print(f"Uplink ports : {uplink_ports}")
print(f"Total ports  : {total_ports}")

# A reminder of why the conversion matters:
# "24" + "2" would give "242" (text joined together), not 26.
