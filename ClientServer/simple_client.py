import socket

# 1. Configuration (The Server's Address)
# This MUST match the HOST and PORT used in the server code.
HOST = '127.0.0.1'
PORT = 65432

# 2. Setup the Client Socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 3. Connect to the Server
    print(f"Attempting to connect to {HOST}:{PORT}...")
    s.connect((HOST, PORT))
    print("Connection successful!")

    # 4. Define and Send Data
    client_message = "Hello, Server! This is the Client."

    # Send the message, converting the string into bytes first
    s.sendall(client_message.encode('utf-8'))
    print(f"Client sent: '{client_message}'")

    # 5. Receive Response
    data = s.recv(1024)

    # Convert the received bytes into a readable string
    server_response = data.decode('utf-8')

    # 6. Display the Response
    print(f"Server response received: {server_response}")

print("Client finished.")
