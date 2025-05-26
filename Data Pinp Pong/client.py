import socket
import time

HOST = 'localhost'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

try:
    while True:
        data = client_socket.recv(1024)
        if not data:
            print("Server disconnected.")
            break
        print(data.decode())
        input("Press Enter to return the packet: ")
        client_socket.sendall(b"Packet returned!")
except:
    print("Connection lost.")

client_socket.close()