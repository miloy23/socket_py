import socket



print("Enter Your server IP address:")

server_host = input()  

print("Enter Your server port Number:")

server_port = int(input())          

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((server_host, server_port))

while True:

    message = input("Enter your message (type 'quit' to exit): ")
    client_socket.send(message.encode('utf-8'))

    if message.lower() == 'quit':
        print("Closing connection.")
        break


    response = client_socket.recv(1024).decode('utf-8')
    print(f"Server response: {response}")


client_socket.close()