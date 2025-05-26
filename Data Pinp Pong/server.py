import socket
import time
import random

HOST = 'localhost'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server is waiting for a client...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

round_num = 1
time_limit = 2.0

while True:
    print(f"\n--- Round {round_num} ---")
    delay = random.uniform(0.5, 1.0)
    time.sleep(delay)

    message = f"Round {round_num}: Respond in {time_limit:.2f} seconds!"
    conn.sendall(message.encode())

    conn.settimeout(time_limit)
    try:
        data = conn.recv(1024)
        if not data:
            print("Client disconnected.")
            break
        print(f"Client responded: {data.decode()}")
        round_num += 1
        time_limit *= 0.9  # increase difficulty
    except socket.timeout:
        print("Client was too slow. Game over!")
        break

conn.close()
server_socket.close()