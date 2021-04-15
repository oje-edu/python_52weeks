from random import choice
import string # full import

# sudo apt install python3-pip -y && sudo pip3 install tabulate
from tabulate import tabulate

from operator import itemgetter
from pprint import pprint

devices = list() # CREATE EMPTY LIST FOR HOLDING DEVICES - devices = [] should work also

# CREATE LOOP TO CREATE LARGE NUMBER OF DEVICES
for index in range(1, 10):
    # CREATE DEVICE DICTIONARY
    device = dict()

    # RANDOM DEVICE NAME
    device["name"] = (
        choice(["r2", "r3", "r4", "r6", "r10"])
        + choice(["L", "U"])
        + choice(string.ascii_letters)
    )

    # RANDOM VENDOR FROM CHOICE OF CISCO, JUNIPER; ARISTA
    device["vendor"] = choice(["cisco", "juniper", "arista"])
    if device["vendor"] == "cisco":
        device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
        device["version"] = choice(["12.1(T).04", "14.07X", "8.12(S).010", "20.25"])
    elif device["vendor"] == "juniper":
        device["os"] = "junos"
        device["version"] = choice(["J6.23.1", "8.43.12", "6.45", "6.03"])
    elif device["vendor"] == "arista":
        device["os"] = "eos"
        device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])
    device["ip"] = "10.0.0." + str(index)

    # NICELY FORMATTED PRINT OF THIS ONE DEVICE
    print()
    for key, value in device.items():
        print(f"{key:>16s} : {value}")

    # ADD THIS DEVICE TO THE LIST OF DEVICES
    devices.append(device)

    # USE PPRINT (prettyprint) TO PRINT DATA AS-IS
    print("\n----- DEVICES AS LIST OF DICTS --------------------")
    pprint(devices)

    # USE 'TABULATE' TO PRINT TABLE OF DEVICES
    print("\n----- SORTED DEVICES IN TABULAR FORMAT ----------------")

    sorted_devices = sorted(devices, key=itemgetter("vendor", "os", "version"))
    print(tabulate(sorted_devices, headers="keys"))
    # -> "short/geek" version: print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))
