import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5555


def receive_messages(client_socket):
    try:
        while True:
            # Receive message from server
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                print(message)
    except Exception as e:
        print(f"Error receiving message: {e}")
        client_socket.close()


def send_messages(client_socket):
    try:
        while True:
            # Send message to server
            message = input()
            client_socket.send(message.encode("utf-8"))
    except Exception as e:
        print(f"Error sending message: {e}")
        client_socket.close()


def start_client():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((HOST, PORT))
    print(f"Connected to server {HOST}:{PORT}")

    # Start threads for sending and receiving messages
    receive_thread = threading.Thread(
        target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()


if __name__ == "__main__":
    start_client()
