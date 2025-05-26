import socket
import calendar
import threading

def weekday(y, m, d):
    re = 'Weekday of birthday: '
    wkd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    x = calendar.weekday(y, m, d)
    r = wkd[x]
    re += f'Year {y}, Month {m}, Day {d} is {r}'
    return re

def handle_client(data, addr, server_socket):
    print(f"[+] Handling client {addr}")
    data = data.decode().strip()
    print("Message from client after decoding:", data)

    try:
        y, m, d = map(int, data.split())
        result = weekday(y, m, d)
    except Exception as e:
        result = f"Invalid input. Error: {e}"

    server_socket.sendto(result.encode(), addr)
    print(f"[-] Finished with client {addr}\n")

# Main UDP server
ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 7504
ss.bind((host, port))

print(f"UDP Server started on {host}:{port}... Waiting for clients")

while True:
    try:
        data, addr = ss.recvfrom(1024)
        print(f"Received data from {addr}")
        thread = threading.Thread(target=handle_client, args=(data, addr, ss))
        thread.start()
    except KeyboardInterrupt:
        print("Server shutting down.")
        break
