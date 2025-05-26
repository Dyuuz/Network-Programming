import socket
import random

def corrupt_packet(data):
    if random.random() < 0.3:  # 30% infection rate
        return data[:-1] + b"?"  # Corrupt last byte
    return data

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 5004))
server_socket.listen(1)

print("Zombie server running...")
conn, addr = server_socket.accept()
while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(corrupt_packet(data))