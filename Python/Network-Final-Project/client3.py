import socket
import threading


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
            if message == 'You have left the chat.':
                break
        except:
            break


def send_message(client_socket):
    while True:
        message = input()
        client_socket.sendall(message.encode())
        if message == '/exit':
            break


if __name__ == "__main__":
    username = input("user name: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connected = False

    while not connected:
        try:
            client.connect(('localhost', 5559))
            connected = True
        except:
            print("Failed to connect. Retrying...")

    client.sendall(username.encode())
    server_response = client.recv(1024).decode()
    print(server_response)

    if server_response == 'Username found. Please enter your password: ':
        password = input("password: ")
        client.sendall(password.encode())

        authentication_result = client.recv(1024).decode()
        print(authentication_result)

        if authentication_result == 'Authentication success':
            threading.Thread(target=receive_messages, args=(client,)).start()
            threading.Thread(target=send_message, args=(client,)).start()
