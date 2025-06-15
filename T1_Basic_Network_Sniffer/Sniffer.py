import socket
import struct

def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('!6s6sH', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

def get_mac_addr(bytes_addr):
    return ':'.join(f'{b:02x}' for b in bytes_addr)

def ipv4_packet(data):
    version_header_len = data[0]
    header_len = (version_header_len & 15) * 4
    ttl, proto, src, target = struct.unpack('!8xBB2x4s4s', data[:20])
    return {
        'version': version_header_len >> 4,
        'header_length': header_len,
        'ttl': ttl,
        'protocol': proto,
        'src_ip': ipv4(src),
        'dst_ip': ipv4(target),
        'data': data[header_len:]
    }

def ipv4(addr):
    return '.'.join(map(str, addr))

def main():
    # Create a raw socket and bind it to the public interface
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    print("[*] Sniffing started... Press CTRL+C to stop.")

    try:
        while True:
            raw_data, addr = conn.recvfrom(65535)
            dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
            print('\nEthernet Frame:')
            print(f'  - Destination: {dest_mac}, Source: {src_mac}, Protocol: {eth_proto}')

            if eth_proto == 8:  # IPv4
                ipv4_data = ipv4_packet(data)
                print('IPv4 Packet:')
                print(f"  - Source: {ipv4_data['src_ip']}, Target: {ipv4_data['dst_ip']}, Protocol: {ipv4_data['protocol']}")
    except KeyboardInterrupt:
        print("\n[*] Sniffing stopped.")

if __name__ == '__main__':
    main()
