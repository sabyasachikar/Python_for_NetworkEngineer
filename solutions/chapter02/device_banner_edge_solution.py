# device_banner_edge_solution.py
# Solution to the Chapter 2 student exercise: a banner for a second device.

hostname = "edge-rtr-02"
mgmt_ip = "10.0.0.2"
vlan_count = 4
uplink_gbps = 1.0
is_reachable = False

print("Device summary")
print("==============")
print(f"Hostname     : {hostname}")
print(f"Management IP: {mgmt_ip}")
print(f"VLAN count   : {vlan_count}")
print(f"Uplink speed : {uplink_gbps} Gbps")
print(f"Reachable    : {is_reachable}")
