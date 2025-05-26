import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

while True:
    msg = input("Send packet: ").encode()
    client.send(msg)  
    data = client.recv(1024)
    print(f"Response: {data.decode()}")
    # client.close()