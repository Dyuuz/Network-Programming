import socket

# Set up the UDP client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 6000

while True:
    # Get user input for date
    date_input = input("Enter your birthdate (YYYY MM DD) or type 'exit' to quit: ")

    if date_input.lower() == 'exit':
        print("Exiting client.")
        break

    # Send the date to the server
    client.sendto(date_input.encode(), (host, port))

    # Receive the result from the server
    result, server_address = client.recvfrom(1024)
    print(f"Server response: {result.decode()}")

client.close()
