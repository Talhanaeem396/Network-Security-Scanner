import socket
from scapy.all import sr1, IP, ICMP

# Function to check open ports
def scan_ports(target_ip, port_range):
    print(f"Scanning ports on {target_ip}...")

    open_ports = []
    for port in range(port_range[0], port_range[1]):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports


# Function to ping a target and check if it's online
def is_online(target_ip):
    print(f"Pinging {target_ip}...")
    pkt = IP(dst=target_ip)/ICMP()
    reply = sr1(pkt, timeout=2, verbose=False)

    if reply:
        return True
    return False


# Main function for scanning
def network_security_scan(target_ip):
    if not is_online(target_ip):
        print(f"Target {target_ip} is not online or unreachable.")
        return

    open_ports = scan_ports(target_ip, (1, 1024))
    if open_ports:
        print(f"Open ports on {target_ip}: {open_ports}")
    else:
        print(f"No open ports found on {target_ip}.")

    print(f"Network security scan for {target_ip} completed.")


if __name__ == "__main__":
    target_ip = input("Enter the IP address to scan: ")
    network_security_scan(target_ip)
