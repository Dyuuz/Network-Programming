import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 5004))

infection_rate = 0
while infection_rate < 100:
    msg = input("Send packet: ").encode()
    client_socket.sendall(msg)
    response = client_socket.recv(1024)
    if b"?" in response:
        infection_rate += 10
        print(f"INFECTED! Rate: {infection_rate}%. Keep going!")
    else:
        print("Packet clean! Try again.")
print("GAME OVER: Fully infected!")