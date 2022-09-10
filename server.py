from concurrent.futures import thread
from http import client, server
from operator import truediv
from telnetlib import IP
from threading import Thread
import socket
from tkinter import SE
from xmlrpc.client import ProtocolError

SERVER= None
IP_ADDRESS= '127.0.0.1'
PORT= 8050
clients={}
BUFFER_SIZE= 4096


def acceptConnections():
    global clients
    global SERVER

    while True:
        client, addr= SERVER.accept()
        print(client.addr)


def setup():
    print('\n\t\t\t\t\t\t\tMUSIC SHARING APP \n')

    global IP_ADDRESS
    global SERVER
    global PORT

    SERVER= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER.listen(100)

    print('\n\t\t\t\tSERVER IS WAITING FOR INCoMING CONNECTIONS...')
    print('\n')

    acceptConnections()


setup_thread= Thread(target=setup)
setup_thread.start()


