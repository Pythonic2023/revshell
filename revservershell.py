import socket
import subprocess

def serv():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servsock:
        servsock.bind(('localhost', 8000))
        servsock.listen(3)
        (sock, addr_info) = servsock.accept()
        print(f'connection from: {addr_info[0]} {addr_info[1]}')
        while True:
            client_message = sock.recv(1024).decode('utf-8')
            if client_message == 'break':
                closing_message = "Closing connection."
                sock.send(closing_message.encode('utf-8'))
                break
            else:
                result = subprocess.run(client_message, capture_output=True)
                sock.send(result.stdout)


if __name__ == '__main__':
    serv()