import socket
import random
import threading

def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

def generate_primes(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

def handle_client(conn, addr):
    print(f"Connected by {addr}")

    greeting = conn.recv(1024).decode()
    print(f"Client says: {greeting}")

    primes = generate_primes(20, 50)
    guess_number = random.choice(primes)
    attempts = 0

    conn.send("Kindly send a number from the received array of prime numbers.".encode())
    conn.send(str(primes).encode())

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                break
            client_num = int(data.strip())
            attempts += 1

            if client_num == guess_number:
                conn.send(f"Congratulations! You guessed the correct prime number {guess_number} in {attempts} attempt(s).".encode())
                break
            elif client_num > guess_number:
                conn.send("Ah ah! The prime number is high. Try again.".encode())
            else:
                conn.send("Hmm! The prime number is low. Try again.".encode())
        except:
            conn.send("Invalid input. Please send a valid prime number.".encode())
    
    conn.close()
    print(f"Game over with {addr}. Total attempts: {attempts}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)
print("Server is listening...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()