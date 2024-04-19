import sys
from scapy.all import *
import json

packetID = 0
log_data = []

def handle_packet(packet):
    print(packet)
    if packet.haslayer(TCP):
        log_data.append({
            'protocol': "TCP",
            'sip': packet[IP].src, 
            'dip': packet[IP].dst, 
            'sp': packet[TCP].sport, 
            'dp': packet[TCP].dport, 
        })
        
    if packet.haslayer(UDP):
        log_data.append({
            'protocol': "UDP",
            'sip': packet[IP].src, 
            'dip': packet[IP].dst, 
            'sp': packet[UDP].sport, 
            'dp': packet[UDP].dport, 
        })



def main(interface):
    try:
        sniff(iface=interface, prn=lambda pkt: handle_packet(pkt), store=0)
    finally:
        log_data_json = json.dumps(log_data, indent=4)
        with open("logdata.json", 'w') as fo:
            fo.write(log_data_json)
        print(f"Log data: \n{log_data}\n")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: python3 netaz.py <interface>")
        sys.exit(1)
    main(sys.argv[1])