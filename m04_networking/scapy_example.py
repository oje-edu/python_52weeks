# HAS TO BE RUN AS SUPERUSER!
# IN TERMINAL: sudo python3 scapy_example.py
# NOTE: SOME TASKS (ICMP ping) MAY TAKE A LONG TIME!
import scapy.all as scapy
from scapy.layers.l2 import Ether, ARP
from scapy.layers.inet import IP, ICMP, TCP

interface = input("Enter your Network-Interface.. hint: ip a on linux or ipconfig/all on windows: ")
subnet = input("Enter your Subnet.. ex. 192.168.177.0/24: ")
# CAPTURE EVERYTHING AND PRINT PACKET SUMMARIES
print("\n----- Packet summaries ----------")
capture = scapy.sniff(iface=interface, count=10)
print(capture.nsummary())

# CAPTURE DNS AND PRINT PACKETS
print("\n----- DNS packet summaries (collect 10 DNS packets ----------")
capture = scapy.sniff(iface=interface, filter="udp port 53", count=10)
print(capture.nsummary())

# CAPTUE ONLY DNS AND PRINT COMPLETE PACKETS
print("\n\n----- DNS packets, complete (collect 10 DNS packets ---------")
capture = scapy.sniff(iface=interface, filter="udp port 53", count=10)
for packet in capture:
    print(packet.show())

# CCAPTURE AND HANDLE PACKETS AS THEY ARRIVE
print("\n\n----- Capture and print packets as sniffed ---------")


def print_packet(pkt):
    print("    ", pkt.summary())


scapy.sniff(iface=interface, prn=print_packet, filter="tcp port https", count=10)

# CAPTURE AND HANDLE PACKTES AS THEY ARRIVE Using LAMBDA
print("\n\n----- Capture and print packets sniffed (using lambda ----------")
scapy.sniff(iface=interface, prn=lambda pkt: print(f"lambda    {pkt.summary()}"), filter="tcp port https", count=10)

# DISCOVER HOSTS ON NETWORK USING MANUAL ARP PING
print("\n\n----- Discovery hosts on network using manual ARP ping ---------")
ans, unans = scapy.srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=subnet), timeout=2)
ans.summary()

# DISCOVER HOSTS ON NETWORK USING ARPING FUNCTION
print("\n\n----- Discovery hosts on network using ARP-ping function --------")
ans, unans = scapy.arping(subnet)
ans.summary()

for res in ans.res:
    print(f"---> IP address discovered: {res[0].payload.pdst}")

# DISCOVER HOSTS ON NETWORKING USING ICMP PING
print("\n\n----- Discovery hosts on network using ICMP ping ----------")
ans, unans = scapy.sr(IP(dst=subnet)/ICMP(), timeout=1)
ans.summary()

# TCP PORT SCAN
print("\n\n----- See what ports are open on device ---------")
while True:

    ip = input("IP address on which to scan ports: ")
    if not ip:
        print("\n----- Ending port scanning")
        break

    answers, unans = scapy.sr(IP(dst=ip)/TCP(flags="S", sport=666, dport=(1, 1024)), timeout=10)
    for answered in answers:
        print(f"---> open port: {answered[0].summary()}")

    print()
    for un_answered in unans:
        print(f"---> closed port: {un_answered[0].summary()}")

    print("\n----- Open/Closed port totals ----------")
    print(f"\tOPen ports: {len(answers)}")
    print(f"\tClosed ports: {len(unans)}")

