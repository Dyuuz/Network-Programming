import socket
import pickle

cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Client Start: ")

host = '127.0.0.1'
port = 7001


msg = input("Enter message to Server: ")
cs.sendto(bytes(msg.encode("ascii")), (host, port))

data, _ = cs.recvfrom(1024)
print(f'Message from Server {data.decode()}')

data, _ = cs.recvfrom(1024)
data_arr = pickle.loads(data)
print("Array Game: ", data_arr)

indexK = input("Enter index from 0 - 3 (bye to quit): ")
while indexK.lower().strip() != 'bye':
    cs.sendto(bytes(indexK.encode("ascii")), (host, port))

    valueK = input("Enter value from 1 - 9: ")
    cs.sendto(bytes(valueK.encode("ascii")), (host, port))

    data, _ = cs.recvfrom(1024)
    if data == b'win':
        print("Server has won ")
        break
    data_arr = pickle.loads(data)
    print(f"Array Game after Client's deduction: {data_arr}")

    data, _ = cs.recvfrom(1024)
    if data == b'win':
        print("Client has won ")
        break
    data_arr = pickle.loads(data)
    print(f"Array Game after Server's deduction: {data_arr}")

    if all(x == 0 for x in data_arr):
        print("Client won and game over!")
        break
    indexK = input("Enter index from 0 to 3 (bye to quit): ")

cs.sendto(b'bye', (host, port))
cs.close()
