import socket

# Creates client socket, connects to server and then starts the shell loop so we can pass commands to the server to then
# execute. We recv the message sent by the server and print it, otherwise we print no data or we have ended the connection
# by typing break to the server.
def shell():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 8000))

    while True:
        command = input('> ')
        sock.send(command.encode('utf-8'))
        message = sock.recv(1024).decode('utf-8')
        if message:
            if message == 'Closing connection.':
                break
            else:
                print(message)
        else:
            print('No data')


if __name__ == '__main__':
    shell()