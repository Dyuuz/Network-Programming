import socket
import random
import json  # For safe serialization

def handle_client(conn):
    # Initialize 3 empty boards (nested lists)
    boards = [[[" " for _ in range(3)] for _ in range(3)] for _ in range(3)]
    
    while True:
        try:
            data = conn.recv(1024).decode().strip()
            if not data:
                break
            
            # Parse input (e.g., "1,2" -> x=1, y=2)
            x, y = map(int, data.split(","))
            player = "X"  # Assume client is always "X"

            # Update 2 random boards
            for b in random.sample(boards, 2):
                b[x][y] = player

            # Send boards as JSON (safe alternative to eval)
            conn.sendall(json.dumps(boards).encode())
            
        except (ValueError, IndexError):
            conn.sendall(b"Invalid move. Use format: x,y (e.g., 1,2)")
    
    conn.close()

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 5000))
    server_socket.listen(1)
    print("Quantum Tic-Tac-Toe Server Running...")
    conn, addr = server_socket.accept()
    handle_client(conn)