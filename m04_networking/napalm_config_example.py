import napalm
import filecmp
import difflib
import sys

print("\n----- connecting to device, comparing configs ---------")
driver = napalm.get_network_driver('ios')
with driver(hostname='192.168.254.200',
            username='cisco',
            password='cisco') as device:

    device.load_merge_candidate(filename="cisco.ios.running.CML-iosv-0.config")
    diff = device.compare_config()
    print("----- DIFF ----------\n", diff)
