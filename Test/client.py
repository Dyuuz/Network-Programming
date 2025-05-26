import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5010))

while True:
    # msg = client.recv(1024).decode()
    # print(msg)

    # for _ in range(3):
    inpt = input("Input an evaluation e.g 4 * 2: ")

    client.send(inpt.encode())

    msg = client.recv(1024).decode()
    print(msg)

    # else:
    #     print("Too many wrong attempts! Moving on...")    

