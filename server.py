import socket


host = '0.0.0.0'  # Listen on all available interfaces
port = 12345       # Choose a port number


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((host, port))


server_socket.listen()

print(f"Server listening on {host}:{port}")


client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

while True:

    data = client_socket.recv(1024).decode('utf-8')
    if not data or data.lower() == 'quit':
        print("Connection closed by client.")
        break

    print(f"Received message: {data}")

    response = input("Enter your response (type 'quit' to exit): ")
    client_socket.send(response.encode('utf-8'))


client_socket.close()
server_socket.close()