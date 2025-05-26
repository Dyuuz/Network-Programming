import time
import random

def data_ping_pong():
    print("Welcome to Data Ping Pong!")
    print("Press Enter as fast as you can to keep the data packet moving.")
    print("Each round gets faster. If you're too slow, the connection crashes.")
    print("Game starts in 3 seconds...\n")
    time.sleep(3)

    round_num = 1
    time_limit = 2.0  # seconds to respond

    while True:
        print(f"--- Round {round_num} ---")
        print("Client: Sending data packet...")

        # Random delay to simulate server processing
        delay = random.uniform(0.5, 1.0)
        time.sleep(delay)

        print("Server: Data packet received. Sending back...")
        start_time = time.time()
        input("Your turn! Press Enter to return the packet: ")
        reaction_time = time.time() - start_time

        if reaction_time > time_limit:
            print(f"\nToo slow! You took {reaction_time:.2f} seconds.")
            print("Connection lost. Game Over!")
            break
        else:
            print(f"Nice! You responded in {reaction_time:.2f} seconds.\n")
            round_num += 1
            time_limit *= 0.9  # make the game faster each round

if __name__ == "_main_":
    data_ping_pong()