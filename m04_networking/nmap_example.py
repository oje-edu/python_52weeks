# HAS TO BE RUN AS SUPERUSER!
# IN TERMINAL: sudo python3 nmap_example.py
# NOTE: SOME TASKS MAY TAKE A LONG TIME!
import nmap
from pprint import pprint

nm = nmap.PortScanner()
subnet = input("Enter you Subnet/CIDR - (ex.: 192.168.177.0/24): ")

while True:

    ip = input("\nInput IP address to scan (or enter to skip): ")
    if not ip:
        break

    print(f"\n----- begin scan of {ip}")
    output = nm.scan(ip, '1-1024', arguments="-sS -sT -sU -O --host-time 600")
    print(f"--- --- command: {nm.command_line()}")

    print("----- nmap scan output -----------")
    pprint(output)

    try:
        pprint(nm[ip].all_tcp())
        pprint(nm[ip].all_udp())
        pprint(nm[ip].all_ip())
    except KeyError as e:
        print(f"   ---> failed to get scan results for {ip}")

    print(f"--- end scan of {ip}")

print("\nExiting nmap scanner")

print("\nScanning all hosts in subnet using l0050r port 22")
nm.scan(subnet, arguments="-p 22 --open")
print("--- iterating hosts with open port 22 (ssh)")
for hosts in nm.all_hosts():
    print("--- --- ", hosts)

print("\nScanning all hosts in subnet using port 80")
nm.scan(subnet, arguments="-p 80 --open")
print("--- iterating hosts with open port 80 (http)")
for hosts in nm.all_hosts():
    print("--- --- ", hosts)

print("\nScanning all hosts in subnet using port 443")
nm.scan(subnet, arguments="-p 443 --open")
print("--- iterating hosts with open port 443 (https)")
for hosts in nm.all_hosts():
    print("--- --- ", hosts)

print("\nScanning all hosts in subnet using ICMP")
nm.scan(subnet, arguments="-PE")
print("--- iterating hosts responding to ICMP echo")
for hosts in nm.all_hosts():
    print("--- --- ", hosts)


def discovered_host(found_host, scan_result):
    if scan_result['nmap']['scanstats']['uphosts'] == '1':
        print(f"--- --- found host: {found_host} scan: {scan_result['nmap']['scanstats']}")


nma = nmap.PortScannerAsync()
print("\nScanning all hosts in subnet using ICMP with callback")
nma.scan(subnet, arguments="-PE", callback=discovered_host)
print("--- iterating hosts responding to ICMP")
while nma.still_scanning():
    nma.wait(5)
