import socket
import threading

def handle_client(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"Connection with {address} closed.")
                break
            print(f"Received from {address}: {message}")
        except Exception as e:
            print(f"Error handling connection with {address}: {e}")
            break

def start_server():
    server_ip = "127.0.0.1"
    server_port = 5555

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"Server listening on {server_ip}:{server_port}")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Accepted connection from {address}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket, address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
