import socket
from threading import Thread
from termcolor import cprint

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 55555))

server.listen(2)

# SEVER ASSIST FUNCTION
def redirect(data : str):
    return data.encode()

# HANDLE THE CONNECTIONS
def handle(connection, players):
    connection.send(redirect("connect"))
    data = connection.recv(1024).decode()
    while True:
        if data:
            cprint(f"RECIEVED :: {data}", "light_blue")
        else:
            connection.close()
            server.close()

# VARIBLES
connections = []
player = 0

while True:
    conn, addr = server.accept()
    cprint(f"Connected to :: {addr}", "green")

    connections.append(conn)
    player += 1

    thread = Thread(target=handle, args=(conn, player,))
    thread.daemon = True
    thread.start()