import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5010))
server.listen(1)
print("Server started...Waiting for client")
conn, addr = server.accept()

while True:
    # conn.send(f"Welcome".encode())

    # for _ in range(3):
    msg = conn.recv(1024).decode()

    if not msg:
        break
    print(f"Evaluation request from {addr}: {msg}")
    msg = eval(msg)
    conn.send(f"The result is: {msg}".encode())