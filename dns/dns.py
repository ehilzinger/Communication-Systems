import socket

# Dictionary to store DNS records
dns_records = {
    'example.com': '192.168.1.100',
    'test.com': '192.168.1.101',
    'google.com': '172.217.1.4'
}


def dns_server():
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to a host and port
    server_socket.bind(('127.0.0.1', 5353))

    print("DNS server listening on port 5353...")

    while True:
        # Receive data from client
        data, address = server_socket.recvfrom(1024)
        domain = data.decode().strip()

        if domain in dns_records:
            ip_address = dns_records[domain]
            response = f"{domain} -> {ip_address}"
        else:
            response = f"No record found for {domain}"

        # Send response to client
        server_socket.sendto(response.encode(), address)


if __name__ == "__main__":
    dns_server()
