import socket
import pickle

def gen_array():
    arr = []
    num = int(input("Enter array length ---> "))
    for i in range(num):
        k = int(input(f"Array value {i}: "))
        arr.append(k)
    return arr

def display_operations():
    print("\nChoose an operation:")
    print("1. Sort ascending")
    print("2. Sort descending")
    print("3. Find max")
    print("4. Find min")
    print("5. Sum")
    print("6. Average")
    print("7. Reverse array")
    print("8. Square each element")
    print("9. Multiply all elements")

def main():
    cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Starting client...")
        host = socket.gethostname()
        port = 6000
        cs.connect((host, port))

        arr = gen_array()
        display_operations()
        choice = int(input("Enter operation number (1-9): "))

        # Send a dictionary with both the array and the chosen operation
        payload = {
            'array': arr,
            'operation': choice
        }

        cs.send(pickle.dumps(payload))  # Send serialized data

        # Receive and display the result from the server
        data = cs.recv(4096)
        result = pickle.loads(data)
        print("Result from server:", result)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        cs.close()

if __name__ == "__main__":
    main()
