import socket
import json  # For safe deserialization

def print_boards(boards):
    for i, board in enumerate(boards):
        print(f"Board {i}:")
        for row in board:
            print("|".join(row))
            print("-" * 5)
        print()

if __name__ == "__main__":
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 5000))

    while True:
        try:
            move = input("Enter x,y (0-2, e.g., 1,2): ").strip()
            client_socket.sendall(move.encode())
            
            # Receive and parse JSON (no eval!)
            response = client_socket.recv(1024).decode()
            if response.startswith("Invalid"):
                print(response)
                continue
            
            boards = json.loads(response)
            print_boards(boards)
            
        except (KeyboardInterrupt, ConnectionError):
            print("\nDisconnected.")
            break

    client_socket.close()