import socket
import pickle
import math
from functools import reduce

def perform_operation(arr, op):
    if op == 1:
        return sorted(arr)
    elif op == 2:
        return sorted(arr, reverse=True)
    elif op == 3:
        return max(arr)
    elif op == 4:
        return min(arr)
    elif op == 5:
        return sum(arr)
    elif op == 6:
        return sum(arr) / len(arr)
    elif op == 7:
        return arr[::-1]
    elif op == 8:
        return [x**2 for x in arr]
    elif op == 9:
        return reduce(lambda x, y: x * y, arr)
    else:
        return "Invalid operation"

# Start server
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Starting server...")

host = socket.gethostname()
port = 6000
ss.bind((host, port))
ss.listen(2)

c, addr = ss.accept()
print(f"Client connected from IP {addr[0]}, port {addr[1]}")

# Receive data from client
data = c.recv(4096)
payload = pickle.loads(data)

arr = payload['array']
op = payload['operation']
print(f"Received array: {arr}")
print(f"Requested operation: {op}")

# Perform operation
result = perform_operation(arr, op)
print("Computed result:", result)

# Send result back to client
c.send(pickle.dumps(result))

c.close()
ss.close()
