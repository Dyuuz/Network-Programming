import socket
import pickle



cs = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
print("Client Start: ")

host = '127.0.0.1'
port = 7001
cs.connect((host, port))

msg = input("Enter message to Server: ")
cs.send(bytes(msg.encode("ascii")))


data = cs.recv(1024).decode()
print(f'Message from Server {data}')

data = cs.recv(1024)
data_arr = pickle.loads(data)
print("Array Game: ", data_arr)


indexK = input("Enter index from 0 - 3 (bye to quit): ")
while indexK.lower().strip() != 'bye':
    cs.send(bytes(indexK.encode("ascii")))

    valueK = input("Enter value from 1 - 9: ")
    cs.send(bytes(valueK.encode("ascii")))

    data = cs.recv(1024)
    if data == b'win':
        print("Server has won ")
        break
    data_arr = pickle.loads(data)
    print(f"Array Game after Client's deduction: {data_arr}")

    data = cs.recv(1024)
    if data == b'win':
        print("Client has won ")
        break
    data_arr = pickle.loads(data)
    print(f"Array Game after Server's deduction: {data_arr}")

    
    if all(x == 0 for x in data_arr):
        print("Client won and game over!")
        break
    indexK = input("Enter index from 0 to 3 (bye to quit): ")

cs.send(b'bye')
cs.close()