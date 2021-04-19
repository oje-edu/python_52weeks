from util.create_utils import create_devices
from pprint import pprint

# --- Main program ------------------------------
if __name__ == '__main__':

    devices = tuple(create_devices(num_devices=4, num_subnets=1))

    print("\n----- LIST OF DEVICES ---------------")
    pprint(devices)


print("\n\n")
print("REMEMBER:")
print("On TUPLES the use of append or extend don't work - IMMUTABLE")
print("But You can reassign the values")
print("or create a new variable an turn the tuple (t) into a list l1 = list(t)")
