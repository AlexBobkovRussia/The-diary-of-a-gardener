import sys

sys.path.append('')
import socket
from time import sleep

host = socket.gethostbyname(socket.gethostname())
port = 51245

clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
s.setblocking(False)


def main_func():
    try:
        data, addr = s.recvfrom(2048)
        if addr not in clients:
            clients.append(addr)
        for client in clients:
            s.sendto(data, client)
    except BlockingIOError:
        pass
    sleep(0.1)
    main_func()


crypt = True

main_func()
