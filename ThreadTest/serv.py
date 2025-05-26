import socket
import threading

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            print(f"Client {addr} disconnected.")
            break
        print(f"Received from {addr}: {data.decode()}")
        conn.sendall(b"ACK")
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)
print("Server listening...")

while True:
    conn, addr = server.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()