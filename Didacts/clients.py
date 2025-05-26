import socket

client_socket = socket.socket()
host = '127.0.0.1'
port = 8006

client_socket.connect((host, port))

# Receive message from server and send request to server
while True:
    message = client_socket.recv(1024).decode()
    print(message)

    # If server sends nothing, break
    if not message:
        break

    expr = input("Enter your input: ")
    client_socket.send(expr.encode())

    result = client_socket.recv(1024).decode()
    print(f"Result from server: {result}")
