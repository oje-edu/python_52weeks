device_str = "   r3-L-n7, cisco, cataclyst 2960, ios , extra stupid stuff "
#NOTE: To make this string iterable using split(",") - so everything after a comma is separate word

# NON LIST COMPREHENSION WAY
device = list()
for item in device_str.split(","):
    device.append(item.strip())
print("\ndevice using for loop:\n\t\t", device)

# LIST COMPREHENSION
device = [item.strip() for item in device_str.split(",")]
print("\ndevice using list comprehension:\n\t\t", device)

# SIMPLER LIST COMPREHENSION
device_info_list = device_str.split(",")
device = [item.strip() for item in device_info_list]
print("\ndevice using simpler list comprehension:\n\t\t", device)

# LIST COMPREHENSION WITH CONDITIONAL
device = [item.strip() for item in device_str.split(",") if "stupid" not in item]
print("\ndevice using list comprehension with conditional:\n\t\t", device)

# TUPLES (IMMUTABLE)
device_info = [
    ("name", "r3-L-n7"),
    ("vendor", "cisco"),
    ("model", "cataclyst 2960"),
    ("os", "ios"),
]

# DICT COMPREHENSION FROM LIST OF TUPLES
device = {item[0]: item[1] for item in device_info}
print("\ndevice using dict comprehension:\n\t\t", device)
print("device nicely formatted:")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

device_info_str = "name:r3-L-n7, vendor:cisco, model:cataclyst 2960, os:ios, version:12.1(T)"

# LIST THEN DICT COMPREHENSION FROM STRING
device_info_pairs = [kv_pair.split(":") for kv_pair in device_info_str.split(",")]
devide = {item[0]: item[1] for item in device_info_pairs}
print("\ndevice using list and dict comprehension:\n\t\t", device)
print("device nicely formatted:")
for key, value in device.items():
    print(f"{key:>16s} : {value}")

# DICT COMPREHENSION FROM STRING
device = {item.split(":")[0]: item.split(":")[1] for item in device_info_str.split(",")}
print("\ndevice using dict comprehension:\n\t\t", device)
print("device nicely formatted:")
for key, value in device.items():
    print(f"{key:>16s} : {value}")