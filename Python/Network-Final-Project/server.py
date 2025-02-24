import socket
import threading
import logging

users = {
    'alireza': '9950',
    'ftm': '1995',
    'amir': '1381',
    'aida': '2020',
}

clients = {}
used_ports = []
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


def find_empty_port(start_port=5555):
    port = start_port
    while port in used_ports:
        port += 1
    return port


def broadcast_message(message):
    for socket in clients.values():
        socket.send(message.encode())


def send_private_message(sender, recipient, message):
    if recipient in clients:
        recipient_socket = clients[recipient]
        recipient_socket.send(f'private message from {sender}: {message}'.encode())
        sender_socket = clients[sender]
        sender_socket.send(f'private message to {recipient}: {message}'.encode())
    else:
        sender_socket = clients[sender]
        sender_socket.send(f'user {recipient} is not online.'.encode())


def handle_client(client_socket, username):
    clients[username] = client_socket

    broadcast_message(f'{username} has joined the chat.')

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == '/exit':
                broadcast_message(f'{username} has left the chat.')
                client_socket.send('You have left the chat.'.encode())
                del clients[username]
                break
            elif message.startswith('/pm'):
                parts = message.split(' ', 2)
                if len(parts) == 3:
                    recipient = parts[1]
                    private_message = parts[2]
                    send_private_message(username, recipient, private_message)
                else:
                    client_socket.send('Correct format: /pm [username] [Message]'.encode())
            else:
                broadcast_message(f'{username}: {message}')
                logging.info(f'{username}: {message}')
        except:
            broadcast_message(f'{username} has left the chat.')
            del clients[username]
            break


def start_server():
    global used_ports
    start_port = 5555

    while True:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        port = find_empty_port(start_port)
        try:
            server.bind(('localhost', port))
            server.listen()

            used_ports.append(port)
            print(f'The server is active on port {port}.')
            logging.info(f'Server started on port {port}')

            while True:
                client_socket, addr = server.accept()
                username = client_socket.recv(1024).decode()

                if username in users:
                    client_socket.send('Username found. Please enter your password: '.encode())
                    password = client_socket.recv(1024).decode()

                    if password == users[username]:
                        client_socket.send('Authentication success'.encode())
                        threading.Thread(target=handle_client, args=(client_socket, username)).start()
                    else:
                        client_socket.send('The password is incorrect'.encode())
                else:
                    client_socket.send('User not found'.encode())

        except OSError as e:
            print(f"Failed to bind port {port}. {e}")
            logging.error(f"Failed to bind port {port}. {e}")
            start_port = port + 1
        finally:
            if port in used_ports:
                used_ports.remove(port)
            server.close()


if __name__ == "__main__":
    start_server()
