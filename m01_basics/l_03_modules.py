from tabulate import tabulate
from util.create_utils import create_devices

# -- MAIN PROGRAM --
if __name__ == '__main__':

    devices = create_devices(num_devices=4, num_subnets=5)

    print("\n", tabulate(devices, headers="keys"))