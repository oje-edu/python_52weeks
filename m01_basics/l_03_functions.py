from random import choice
import string
from tabulate import tabulate


def create_devices(num_devices=1, num_subnets=1):
    # CREATE LIST OF DEVICES
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("ALTA: hast du deinen Fachinformatiker bei der IHK gewonnen ?? viel zu viele Geräte/Subnetze angefordert")
        return created_devices

    for subnet_index in range(1, num_subnets + 1):

        for device_index in range(1, num_devices + 1):

            # CREATE DEVICE DICTIONARY
            device = dict()

            # RANDOM DEVICE NAME
            device["name"] = (
                    choice(["r2", "r4", "no4", "r10"])
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
            device["ip"] = "10.0.0." + str(subnet_index) + "." + str(device_index)

            created_devices.append(device)
    return created_devices


# -- MAIN PROGRAM --
if __name__ == '__main__':
    devices = create_devices(num_devices=20, num_subnets=4)
    print("\n", tabulate(devices, headers="keys"))
