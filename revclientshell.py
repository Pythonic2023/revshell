import socket
import time

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