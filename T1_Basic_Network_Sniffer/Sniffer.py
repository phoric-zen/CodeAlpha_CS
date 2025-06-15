# sniffer.py

from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

def main():
    print("🔍 Starting packet sniffer on Windows...\nPress Ctrl+C to stop.\n")
    
    # Start sniffing packets on the default interface
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
