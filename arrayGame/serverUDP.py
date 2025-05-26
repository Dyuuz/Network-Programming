import socket
import random
import pickle

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

def handle_client(data, addr, ss):
    print(f'Client {addr} connected.')

    data = data.decode()
    print(f'message with decoding {data}')

    msg = input("Send index and corresponding values: ")
    ss.sendto(bytes(msg.encode("ascii")), addr)

    genArray()
    print("Array Game: ", arr)
    data_arr = pickle.dumps(arr)
    ss.sendto(data_arr, addr)

    while True:
        data, addr = ss.recvfrom(1024)
        data = data.decode()
        if data.lower().strip() == 'bye':
            print("Game Over")
            break
        indexK = int(data)

        data, addr = ss.recvfrom(1024)
        valueK = int(data)

        indS = genIndex()
        valS = genValue()

        print(f"Client Index {indexK} and Value {valueK}")
        print(f"Server Index {indS} and Value {valS}")

        if pop(arr, M, indexK, valueK):
            print("Array Game after Client's deduction: ", arr)
            data_arr = pickle.dumps(arr)
            ss.sendto(data_arr, addr)
        else:
            ss.sendto(pickle.dumps(arr), addr)

        if isWinner(arr):
            ss.sendto(b'win', addr)
            print("Client has Won")
            break

        if pop(arr, M, indexK, valueK):
            print("Array Game after Server's deduction: ", arr)
            data_arr = pickle.dumps(arr)
            ss.sendto(data_arr, addr)
        else:
            ss.sendto(pickle.dumps(arr), addr)

        if isWinner(arr):
            ss.sendto(b'win', addr)
            print("Server has Won")
            break

ss = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
print("Server Start: ")

host = '127.0.0.1'
port = 7001
ss.bind((host, port))

while True:
    data, addr = ss.recvfrom(1024)
    handle_client(data, addr, ss)
