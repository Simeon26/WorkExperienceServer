import socket
import _thread

client_sockets = []


def handle_client(client_socket, address):
    while True:
        data = client_socket.recv(1024).decode()
        print("Message recieved from '", address, "': ", data.encode())

        if not data:
            break

        for client in client_sockets:
            client.send(data.encode())

    client_socket.close()
    client_sockets.remove(client_socket)


def main():
    port = 8080

    server_socket = socket.socket()
    server_socket.bind(('', port))
    print("Listening on", port)

    # 100 defines maximum number of simultatious clients
    server_socket.listen(100)

    while True:
        connection, address = server_socket.accept()
        client_sockets.append(connection)
        _thread.start_new_thread(handle_client,(connection,address))

    server_socket.close()


if __name__ == '__main__':
    main()

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8080))
clientsocket.send('hello')