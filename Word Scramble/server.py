import socket, random

# Load words from the text file
with open("words.txt", "r") as file:
    words = [line.strip() for line in file if line.strip()]
             
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5015))
server.listen(1)
print("Server started...Waiting for client")
conn, addr = server.accept()

while True:
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    conn.send(f"SCRAMBLE:{scrambled}".encode())

    for i in range(3):
        guess = conn.recv(1024).decode()
        if guess == "quit":
            conn.send(b"Bye! Game over.")
            conn.close(); break
        
        elif guess == "hint":
            conn.send(f"Hint: starts with '{word[0]}' and ends with '{word[-1]}'".encode())

        elif guess == word:
            conn.send(b"Correct! +10 Points")
            time_taken = conn.recv(1024).decode()
            print(f"{addr} solved '{word}' in {time_taken} seconds.")
            break
        else:
            conn.send(b"Wrong! Try again.")
            print()