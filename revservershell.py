import socket
import subprocess


# This function creates a server socket which listens for incoming connections. Upon connecting it shows the IP and
# port number associated with the connection. If from the client "break" is given to the server, the server and client
# both shutdown gracefully. You can run shell commands and get their stdout to the client when communicating with the
# server.
def serv():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servsock:
        servsock.bind(('localhost', 8000))
        servsock.listen(3)
        (sock, addr_info) = servsock.accept()
        print(f'connection from: {addr_info[0]} {addr_info[1]}') # print the IP and port of connection
        while True:
            client_message = sock.recv(1024).decode('utf-8')
            if client_message == 'break':
                closing_message = "Closing connection."
                sock.send(closing_message.encode('utf-8'))
                break
            else:
                execute_command(client_message, sock)

# When you pass a command that is something other than break, this function will be called and the result will be passed
# To the client socket communicating with the server. pass our client message/command and sock to execute_function.
def execute_command(command, sock):
    # pass the shell=True so we can execute shell commands the same as we would with a shell, otherwise doing "cat file"
    # would fail and would return 'cat file' file or directory not found. capture output to have both STDOUT and STDERR
    # captured.
    result = subprocess.run(command, shell=True, capture_output=True)
    # Send stderr is return code not 0, otherwise send stdout back to the client.
    if result.returncode != 0:
        sock.send(result.stderr)
    else:
        sock.send(result.stdout)


if __name__ == '__main__':
    serv()