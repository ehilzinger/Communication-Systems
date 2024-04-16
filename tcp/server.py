import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5555

# List to store client connections
clients = []


def handle_client(client_socket, client_address):
    try:
        while True:
            # Receive message from client
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(f"Received from {client_address}: {message}")
                # Broadcast message to all clients
                broadcast(message, client_socket)
            else:
                # If no data received, close connection
                clients.remove(client_socket)
                client_socket.close()
                break
    except Exception as e:
        print(f"Error: {e}")
        clients.remove(client_socket)
        client_socket.close()


def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode("utf-8"))
            except Exception as e:
                print(f"Error broadcasting message: {e}")
                clients.remove(client_socket)
                client_socket.close()


def start_server():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))
    # Start listening for incoming connections
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}...")

    while True:
        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")
        # Add client socket to the list
        clients.append(client_socket)
        # Start a new thread to handle the client
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == "__main__":
    start_server()
