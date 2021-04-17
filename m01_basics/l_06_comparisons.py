from util.create_utils import create_devices
from pprint import pprint
from random import randint, uniform
from datetime import datetime

devices = create_devices(num_subnets=2, num_devices=25)

print("#######################################")
print("# NOTE:                               #")
print("# THAT ALL DATA IS RANDOMLY GENERATED #")
print("#######################################")

print("\n  NAME       VENDOR : OS       IP ADDRESS      VERSION")
print("  -----     -------   -----   -------------    -----------")
for device in devices:
    print(
        f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}  {device["ip"]:<15}  {device["version"]}'
    )

print("\n\nONLY SHOW CISCO DEVICES")
print("\n  NAME       VENDOR : OS       IP ADDRESS      VERSION")
print("  -----     -------   -----   -------------    -----------")
for device in devices:
    if device["vendor"].lower() == "cisco":
        print(
            f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}  {device["ip"]:<15}  {device["version"]}'
        )

print("\n\nDONT SHOW CISCO DEVICES")
print("\n  NAME       VENDOR : OS       IP ADDRESS      VERSION")
print("  -----     -------   -----   -------------    -----------")
for device in devices:
    if device["vendor"].lower() != "cisco":
        print(
            f'{device["name"]:>7}  {device["vendor"]:>10} : {device["os"]:<6}  {device["ip"]:<15}  {device["version"]}'
        )

print("\n----- Starting comparison of device names (looking for duplicates)-----")
for index, device_a in enumerate(devices):
    for device_b in devices[index+1:]:
        if device_a["name"] == device_b["name"]:
            print(f"Found match! {device_a['name']} for both {device_a['ip']} and {device_b['ip']}")
print("----- Comparison of device names completed")

print("\n\nFIRST FOUND VERSION WILL SET TO STANDARD VERSION")
print("\n----- Create table of arbitrary 'standard' versions of each vendor:os ---------")
standard_versions = dict()
for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    if vendor_os not in standard_versions:
        standard_versions[vendor_os] = device["version"]
pprint(standard_versions)

print("\n----- Create list of non-compliant device OS versions for each vendor:os --------")
non_compliant_devices = dict()
for vendor_os, _ in standard_versions.items():
    non_compliant_devices[vendor_os] = []

for device in devices:
    vendor_os = device["vendor"] + ":" + device["os"]
    if device["version"] != standard_versions[vendor_os]:
        non_compliant_devices[vendor_os].append(device["ip"] + " version: " + device["version"])

pprint(non_compliant_devices)

print("\n\n----- Assignment, copy, and deep copy -----")
devices2 = devices
devices[0]["name"] = "kein schlauer Gerätename"
if devices2 == devices:
    print("\n    Assignment and modification: devices2 STILL equals devices")
    print("   ---> Die Moral von der Geschicht: Assignment is NOT the same as copy!")
else:
    print("    Hä?")

from copy import copy
from copy import deepcopy

devices2 = copy(devices)
devices2[0]["name"] = "Diggha das ist immernoch kein schlauer Gerätename"
if devices2 == devices:
    print("\n   Shallow copy and modification: devices2 STILL equals devices")
    print(" ---> Die Moral von der Geschicht: 'copy()' only uses SHALLOW (1st level) copy!")
    print(" ---> Ergebnis: HAHA - I just screwed up the original version!!")
else:
    print("    Hä?")

devices2 = deepcopy(devices)
devices2[0]["name"] = "Hier mal ein ganz schlauer Gerätename"
if devices2 == devices:
    print("    Hä?")
else:
    print("\n   Deepcopy and modification: devices2 no longer equals devices")
    print(" ---> Die Moral von der Geschicht: 'deepcopy()' gives you a complete copy of the original!")
    print(" ---> Ergebnis: I can do whatever I want with my copy, without touching the original")

new_set_of_devices = create_devices(num_subnets=2, num_devices=25)
if new_set_of_devices == devices:
    print("    Hä?")
else:
    print("\n   Comparisons of complex, deep data is easy in Python")
    print(" ---> Die Moral von der Geschicht: you can compare any two data structures, no matter how deeply nested")

print("\n\n----- Comparison for implementing SLAs ------------\n")
SLA_AVAILABILITY = 98
SLA_RESPONSE_TIME = 1.0

devices = create_devices(num_subnets=2, num_devices=25)
for device in devices:
    device["availability"] = randint(94, 100)
    device["response_time"] = uniform(0.5, 1.1)

    if device["availability"] < SLA_AVAILABILITY:
        print(f"{datetime.now()}: {device['name']:6} - Availability {device['availability']} < {SLA_AVAILABILITY}")
    if device["response_time"] > SLA_RESPONSE_TIME:
        print(f"{datetime.now()}: {device['name']:6} - Response Time {device['response_time']:.3f} > {SLA_RESPONSE_TIME}")

print("\n\n----- Comparing classes -----------")

class DeviceWithEq:

    def __init__(self, name, ip):
        self.name = name
        self.ip_address = ip
    def __eq__(self, other):
        if not isinstance(other, DeviceWithEq):
            return False
        return self.name == other.name and self.ip_address == other.ip_address

d1 = DeviceWithEq("device 1", "10.10.10.1")
d1_equal = DeviceWithEq("device 1", "10.10.10.1")
d1_different =DeviceWithEq("device 2", "10.10.10.2")

print("\n    Comparison with an __eq__ method to handle evaluation")
if d1 == d1_equal:
    print(f"   ---> using __eq__ : success: {d1} equals {d1_equal}")
else:
    print(f"    !!! using __eq__ : UARG, classes not equal and they should be")
if d1 == d1_different:
    print(f"    !!! using __eq__ : UARG, classes equal and they should not be")
else:
    print(f"   ---> using __eq__ : success: {d1} not equal to {d1_different}")

class DeviceWithNoEq:

    def __init__(self, name, ip):
        self.name = name
        self.ip_address = ip

d1 = DeviceWithNoEq("device 1", "10.10.10.1")
d1_equal = DeviceWithNoEq("device 1", "10.10.10.1")
d1_same = d1

print("\n    Comparison WITHOUT an __eq__ method to handle evaluation")
if d1 == d1_equal:
    print(f"    !!! with no __eq__ : Oops, didn't expect this")
else:
    print(f"    ---> with no __eq__ : success: not equal, as expected")
if d1 == d1_same:
    print(f"    ---> with no __eq__ : success: {d1} points to same object instance as {d1_same}")
else:
    print(f"    !!! with no __eq__ : Oops, didn't expect this")
