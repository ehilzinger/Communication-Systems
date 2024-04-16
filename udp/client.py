import socket
import threading

# Function to receive messages


def receive_messages():
    while True:
        try:
            data, addr = client_socket.recvfrom(1024)
            print(data.decode())
        except:
            print("An error occurred while receiving messages.")
            break

# Function to send messages


def send_message():
    while True:
        message = input()
        client_socket.sendto(message.encode(), server_address)


# Get the IP address and port of the server
server_ip = input("Enter the IP address of the server: ")
server_port = int(input("Enter the port of the server: "))
server_address = (server_ip, server_port)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind a random port for receiving messages
client_socket.bind(('', 0))

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Start sending messages
send_message()
