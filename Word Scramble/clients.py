import socket, time

client = socket.socket()
client.connect(('localhost', 5015))
score = 0
print("Welcome to Networking Word Puzzle Game")

while True:
    msg = client.recv(1024).decode()
    if msg.startswith("SCRAMBLE:"):
        word = msg.split(":")[1]
        print(f"\nYou have 3 attempts to Unscramble this word: {word}")
        start = time.time()

        for i in range(3):
            guess = input("Your guess (or 'hint', 'quit'): ")
            client.send(guess.encode())
            response = client.recv(1024).decode()
            print(response)

            if "Correct!" in response:
                end = time.time()
                time_taken = round(end - start, 2)
                client.send(str(time_taken).encode())
                print(f"Time taken: {time_taken} seconds")
                score += 10
                break

            if "Bye!" in response:
                print("Game ended. Final Score:", score)
                client.close(); exit()
        else:
            print("Too many wrong attempts! Moving on...")