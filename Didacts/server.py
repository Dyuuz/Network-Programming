import socket
from _thread import *
import os

# Custom function to calculate the result of a simple arithmetic expression
# (e.g., '4 + 5'). This is a placeholder; you can replace it with your own logic.
def calculate(expression):
    """Safely evaluates a simple arithmetic expression like '4 + 5'."""
    try:
        result = eval(expression)  # Be cautious with eval
        return str(result)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except Exception:
        return "Invalid input. Use format like: 3 + 4"

# Function to handle client connections
def client_handler(con):
    while True:
        try:
            con.send(str.encode("Enter operation (e.g., 4 + 5): "))
            data = con.recv(1024).decode()

            if not data:
                break  # Client disconnected

            print(f"Received: {data}")
            result = calculate(data)  # Call your function here
            print(f"Client result data: {data}")
            con.send(result.encode())

        except:
            break

    con.close()
    print("Client disconnected.")

# Define the server socket, bind it to a host and port, and listen for incoming connections
# This is a simple TCP server that handles multiple clients using threads.
server_socket = socket.socket()
host = '127.0.0.1'
port = 8006
server_socket.bind((host, port))
server_socket.listen(5)

print("Server started. Waiting for clients...")

# Main Server Loop - Accept incoming connections as much as 5 clients at a time
# and start a new thread for each client using the client_handler function.
while True:
    con, addr = server_socket.accept()
    print(f"Connected to: {addr}")
    start_new_thread(client_handler, (con,))
