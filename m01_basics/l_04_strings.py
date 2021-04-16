from pprint import pprint

device1_str = " r3A-L-liF3, cisco, cataclyst 2960, ios "

# SPLIT
print("STRING STRIP, SPLIT, REPLACE")
device1 = device1_str.split(",")
print("device1 using SPLIT:")
print("   ", device1)

# STRIP (remove blank in beginning and end)
device1 = device1_str.strip().split(",")
print("device1 using STRIP and SPLIT:")
print("   ", device1)

# REMOVE BLANKS
device1 = device1_str.replace(" ", "").split(",")
print("device1 replaced blanks using split:\n   ", device1)

# REMOVE BLANKS, CHANGE COMMA TO COLON (result is just a string)
device1_str_colon = device1_str.replace(" ", "").replace(",", ":")
print("device1 replaced blanks, comma to colon:")
print("    ", device1_str_colon)

# LOOP WITH STRIP AND SPLIT
device1 = list()
for item in device1_str.split(","):
    device1.append(item.strip())
print("device1 using loop and strip for each item:")
print("    ", device1)

# STRIP AND SPLIT, SINGLE LINE USING LIST COMPREHENSION
device1 = [item.strip() for item in device1_str.split(",")]
print("device1 using LIST COMPREHENSION:")
print("    ", device1)

# IGNORING CASE
print("\n\nIGNORING CASE")
model = "IHK0815V21"
if model == "ihk0815v21":
    print(f"matched: {model}")
else:
    print(f"didn't match: {model}")

model = "IHK0815V21"
if model.lower() == "iHk0815v21".lower():
    print(f"matched using lower(): {model}")
else:
    print(f"didn't match: {model}")

# FINDING SUBSTRING
print("\n\nFINDING SUBSTRING")
version = "Virtual XE Software (x86_64_LINUX_ISOD-UNIVERSAL),Version 08.15_21, RELEASE SOFTWARE (fc1)"
expected_version = "Version 08.15_21"
index = version.find(expected_version)
if index >= 0:
    print(f"found version: {expected_version} at location {index} ")
else:
    print(f"not found: {expected_version}")

# SEPARATING STRING COMPONENTS
print("\n\nSEPARATING VERSION STRING COMPONENTS")
version_info = version.split(",")
for part_no, version_info_part in enumerate(version_info):
    print(f"version part {part_no}: {version_info_part.strip()}")

show_interface_stats = """
GigabitEthernet1
        Switching path      Pkts In     Chars In    Pkts Out    Chars Out
             Processor        25678      1676769        7656      4673889
           Route cache            0            0           0            0
     Distributed cache       677488      7668898      887890     65444789
                 Total       703166      9345667      895546     70118678
GigabitEthernet2
        Switching path      Pkts In     Chars In    Pkts Out    Chars Out
             Processor           19         1140           0            0
           Route cache            0            0           0            0
     Distributed cache         6077       663304           0            0
                 Total         6096       664444           0            0
Interface GigabitEthernet3 is disabled

Loopback21
        Switching path      Pkts In     Chars In    Pkts Out    Chars Out
             Processor            0            0           0            0
           Route cache            0            0           0            0
     Distributed cache            0            0           0            0
                 Total            0            0           0            0
Loopback55
        Switching path      Pkts In     Chars In    Pkts Out    Chars Out
             Processor            0            0           3          241
           Route cache            0            0           0            0
     Distributed cache            0            0           0            0
                 Total            0            0           3          241
Loopback100
        Switching path      Pkts In     Chars In    Pkts Out    Chars Out
             Processor            0            0          43         2806
           Route cache            0            0           0            0
     Distributed cache            0            0           0            0
                 Total            0            0          43         2806                                         
"""

interface_counters = dict()
show_interface_stats_lines = show_interface_stats.splitlines()
for index, stats_line in enumerate(show_interface_stats_lines):
    if stats_line.find('GigabitEthernet', 0) == 0:

        totals_line = show_interface_stats_lines[index + 5]
        interface_counters[stats_line] = totals_line.split()[1:]

print("\n\n----- Interface Counters -------------------")
pprint(interface_counters)

show_arp = """
Protocol  Address          Age (min)  Hardware Addr  Type  Interface
Internet  10.90.0.1                -  0050:56bb:e99c  ARPA  GigabitEthernet
Internet  10.90.0.100             20  0050:56bb:8aff  ARPA  GigabitEthernet
Internet  10.90.0.254              0  0050:56bb:b00b  ARPA  GigabitEthernet
"""

arp_table = dict()
for arp_line in show_arp.splitlines():
    if arp_line.lower().find("internet", 0) == 0:
        # manually count the values that get in to the []
        arp_table[arp_line[10:25].strip()] = arp_line[38:52]

print("\n\n----- ARP Table -------------------")
pprint(arp_table)