import socket
from threading import Thread
from termcolor import cprint
from sys import exit

# SERVER SETUP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 55555))

# SERVER CONNECTION
server.listen(2)
cprint("SERVER STARTED, WAITING FOR CONNECTIONS...", "blue")

# SEVER ASSIST FUNCTION
def redirect(data : str):
    return data.encode()

# HANDLE THE CONNECTIONS
def handle(connection, players):
    connection.send(redirect("connect"))
    data = connection.recv(1024).decode()
    while True:
        try:
            if data:
                cprint(f"RECIEVED :: {data}", "magenta")
                data = connection.recv(1024).decode()
            else:
                connection.close()
                server.close()
        except KeyboardInterrupt:
            cprint("CLOSING SERVER...", "red")

# VARIBLES
connections = []
player = 0

while True:
    try:
        conn, addr = server.accept()
        cprint(f"Connected to :: {addr}", "grey")

        connections.append(conn)
        player += 1

        thread = Thread(target=handle, args=(conn, player,))
        thread.daemon = True
        thread.start()

    except OSError:
        cprint("CLOSING SERVER...", "red")
        server.close()
        exit()