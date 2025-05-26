import socket
import random
import pickle
from _thread import*
import os

arr = []
N = 4
M = 9

def genArray():
    global arr
    arr = []
    for i in range(N):
        x = random.randint(1, M)
        arr.append(x)

def genIndex():
    return random.randint(0, N-1)

def genValue():
    return random.randint(1, M)

def pop(arr, M, index, value):
    if index < 0 or index >= N:
        print("Index Error (Out of range)")
        return False
    if value > arr[index] or value < 0:
        print("Impossible to subtract less value")
        return False
    else:
        arr[index] = arr[index] - value
        return True

def isWinner(arr):
    return all(x == 0 for x in arr)


def handle_client(ss2):
    addr = ss2.getpeername()  
    print(f'Client {addr[0]} connected.')

    data = ss2.recv(1024)
    print(f'message without decoding {data}')
    data = data.decode()
    print(f'message with decoding {data}')

    msg = input("Send index and corresponding values: ")
    ss2.send(bytes(msg.encode("ascii")))

    genArray()
    print("Array Game: ", arr)
    data_arr = pickle.dumps(arr)
    ss2.send(data_arr)

    while True:
        data = ss2.recv(1024).decode()
        if data.lower().strip() == 'bye':
            print("Game Over")
            break
        indexK = int(data)

        data = ss2.recv(1024).decode()
        valueK = int(data)

        indS = genIndex()
        valS = genValue()

        print(f"Client Index {indexK} and Value {valueK}")
        print(f"Server Index {indS} and Value {valS}")

        if pop(arr, M, indexK, valueK):
            print("Array Game after Client's deduction: ", arr)
            data_arr = pickle.dumps(arr)
            ss2.send(data_arr)
        else:
            ss2.send(pickle.dumps(arr))

        if isWinner(arr):
            ss2.send(b'win')
            print("Client has Won")
            break

        if pop(arr, M, indexK, valueK):
            print("Array Game after Server's deduction: ", arr)
            data_arr = pickle.dumps(arr)
            ss2.send(data_arr)
        else:
            ss2.send(pickle.dumps(arr))

        if isWinner(arr):
            ss2.send(b'win')
            print("Server has Won")
            break

    ss2.close()


ss = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM)
print("Server Start: ")

host = '127.0.0.1'
port = 7001
ss.bind((host, port))
ss.listen(4)


th = 0
while True:
    ss2, addr = ss.accept()
    print(f'Connected to client {addr[0]} on port {addr[1]}')
    start_new_thread(handle_client, (ss2,)) 
    th += 1
    print(f'Thread no {th} and process id {os.getpid()}')
    

        