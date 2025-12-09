import socket
import threading

COMMON_PORTS = {
    21: "FTP (Insecure)",
    22: "SSH",
    23: "Telnet (Insecure)",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3 (Insecure)",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8080: "HTTP-Alt"
}

open_ports = []

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))
        if result == 0:
            service = COMMON_PORTS.get(port, "Unknown Service")
            open_ports.append((port, service))
        sock.close()
    except:
        pass

def main():
    target = input("Enter Target IP: ")

    print(f"\nScanning {target}...\n")

    threads = []
    for port in range(1, 1025):     # Scans first 1024 ports
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    if open_ports:
        print("Open Ports Found:\n")
        for port, service in open_ports:
            print(f"Port {port}: {service}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()
