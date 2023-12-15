from sys import exit
from termcolor import cprint
import socket
import pygame

# INITIAL SCREEN SETUP
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fruit Rivals")

# NETWORK SETUP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((socket.gethostname(), 55555))

# TESTING SERVER CONNECTION
TEST_DATA = server.recv(1024).decode()
cprint(f"RECIEVED :: {TEST_DATA}", "light_yellow")

#! EVENT HANDLER !
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()