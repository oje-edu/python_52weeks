from pprint import pprint
from random import choice
import copy

from util.create_utils import create_network

device =  {
    "name": "r3a-L-n4",
    "vendor": "cisco",
    "model": "cataclyst 2960",
    "os": "ios",
    "interfaces": [

    ]
}

print("\n\n----- devices with no interfaces --------------")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

interfaces = list()
for index in range(0, 8):
    interface = {
        "name": "g/0/0/" + str(index),
        "speed": choice(["10", "100", "1000"])
    }
    interfaces.append(interface)
device["interfaces"] = interfaces

print("\n\n----- devices with interfaces --------------")
for key, value in device.items():
    if key != "interfaces":
        print(f"{key:>16s} : {value}")
    else:
        print(f"{key:>16s} :")
        for interface in interfaces:
            print(f"\t\t\t\t\t{interface}")
print()
print("\n\n---- devices with interfaces using p(retty)print")
pprint(device)

print("\n\n----- network with devices and interfaces -------------")
network = create_network(num_devices=4, num_subnets=4)
pprint(network)

print("\n----- information about the network ---------------")
print(f"-- number of subnets: {len(network['subnets'])}")
print(f"-- list of subnets:   {network['subnets'].keys()}")
print(f"-- list of subnets w/o extraneous: {', '.join(network['subnets'])}")

print("\n----- network and devices nicely formatted ---------------")
for subnet_address, subnet in network["subnets"].items():
    print(f"\n-- subnet: {subnet_address}")
    for device in subnet["devices"]:
        print(f"   |-- device: {device['name']:8} {device['ip']:10} {device['vendor']:>10} : {device['os']}")

print("\n\n----- Remember, Remember The 5th Of November, assignment vs shallow copy vs deep copy -----")
print("       modify 'network' only, and see if assign/copy/deepcopy versions reflect the change")
network_assign = network
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "different name assigned"
print(f"    --- network != network_assign :   {network!=network_assign}")

network_copy = copy.copy(network)
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "another different name, copy this time"
print(f" --- network != network_copy :    {network!=network_copy}")

network_deepcopy = copy.deepcopy(network)
network["subnets"]["10.0.1.0"]["devices"][0]["name"] = "athis is with deep copy"
print(f" --- network != network_deepcopy :    {network!=network_deepcopy}")