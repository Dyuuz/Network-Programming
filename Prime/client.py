import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

# Send initial message
client.send(b"hello server, I want to play with you")

# Receive server's response and array
print(client.recv(1024).decode())  # Server's greeting
primes = eval(client.recv(1024).decode())  # Prime array
print(f"Received primes: {primes}")

# Play guessing game
while True:
    try:
        guess = input("Pick a prime number from the list: ")
        if guess.strip().isdigit() and int(guess) in primes:
            client.send(guess.encode())
            response = client.recv(1024).decode()
            print(response)
            if "Congratulations" in response:
                break
        else:
            print("Please choose a valid prime number from the list.")
    except Exception as e:
        print(f"Error: {e}")
        break

client.close()