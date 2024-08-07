import socket
import threading

# Сервер
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 1234))
    server_socket.listen(1)
    print("Server is listening on localhost:1234")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection established with {address}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"Received message: {message}")
            response = input("Enter response: ")
            client_socket.send(response.encode('utf-8'))

        client_socket.close()

# Клиент
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 1234))
    print("Connected to server")

    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode('utf-8'))
        data = client_socket.recv(1024)
        response = data.decode('utf-8')
        print(f"Received response: {response}")

    client_socket.close()

# Запуск сервера и клиента
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python chat.py server/client")
        sys.exit(1)

    mode = sys.argv[1]
    if mode == 'server':
        server()
    elif mode == 'client':
        client()
    else:
        print("Invalid mode. Please specify 'server' or 'client'.")