from random import choice
import string


def create_device(device_index, subnet_index):

    device = dict()

    # RANDOM DEVICE NAME
    device["name"] = (
            choice(["IHK", "BRD", "no4", "r10"])
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
        device["version"] = choice(["2.45.1F", "2.55", "2.92.145", "3.01"])

    device["ip"] = "10.0." + str(subnet_index) + "." + str(device_index)

    return device


def create_devices(num_devices=1, num_subnets=1):
    # CREATE LIST OF DEVICES
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("ALTA: hast du deinen Fachinformatiker bei der IHK gewonnen ?? viel zu viele Geräte/Subnetze angefordert")
        return created_devices

    print("beginning device creation")
    for subnet_index in range(1, num_subnets + 1):

        for device_index in range(1, num_devices + 1):

            device = create_device(device_index, subnet_index)
            created_devices.append(device)

            print(".", end="")
    print("completed device creation")
    return created_devices


def create_network(num_devices=1, num_subnets=1):
    devices = create_devices(num_devices, num_subnets)

    network = dict()
    network["subnets"] = dict()

    for device in devices:
        subnet_address_bytes = device["ip"].split(".")
        subnet_address_bytes[3] = "0"
        subnet_address = ".".join(subnet_address_bytes)

        if subnet_address not in network["subnets"]:

            network["subnets"][subnet_address] = dict()
            network["subnets"][subnet_address]["devices"] = list()

        network["subnets"][subnet_address]["devices"].append(device)

        interfaces = list()
        for index in range(0, choice([2, 4, 8])):
            interface = {
                "name": "g/0/0/" + str(index),
                "speed": choice(["10", "100", "1000"])
            }
            interfaces.append(interface)
    return network


def create_devices_gen(num_devices=1, num_subnets=1):

    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets requested")
        return None

    print("beginning device creation")
    for subnet_index in range(1, num_subnets + 1):

        for device_index in range(1, num_devices + 1):
            device = create_device(device_index, subnet_index)
            # no return for generator
            yield device

