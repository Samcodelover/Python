import socket

# 1. Configuration (The Address)
# Use '127.0.0.1' or 'localhost' for testing on your own computer.
HOST = '127.0.0.1'
PORT = 65432  # Use a high number port that isn't commonly used (must be > 1024)

# 2. Setup the Server Socket
# AF_INET is for IPv4; SOCK_STREAM is for TCP (reliable data transfer)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # 3. Bind the address to the socket
    s.bind((HOST, PORT))

    # 4. Start listening for incoming connections (up to 1 client queue)
    s.listen()
    print(f"Server listening on {HOST}:{PORT}")

    # 5. Accept a connection
    # 'conn' is the new socket dedicated to this client.
    # 'addr' is the client's address.
    conn, addr = s.accept()

    with conn:
        print(f"Connected by {addr}")

        # 6. Receive Data
        # We try to receive up to 1024 bytes of data.
        data = conn.recv(1024)

        # Convert the received bytes into a readable string
        message = data.decode('utf-8')
        print(f"Client message received: {message}")

        # 7. Process and Send Response
        response = f"Server received your message: '{message}'"

        # Send the response back, first converting the string to bytes
        conn.sendall(response.encode('utf-8'))

print("Server finished.")