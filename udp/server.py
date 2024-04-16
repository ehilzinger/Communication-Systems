import socket

# Get the IP address and port for the server
server_ip = "127.0.0.1"  # Localhost
server_port = 12345  # Choose any available port

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
server_socket.bind((server_ip, server_port))

print("Server is running on", server_ip + ":" + str(server_port))

# Receive and print incoming messages
while True:
    data, addr = server_socket.recvfrom(1024)
    print(data.decode(), "from", addr)
