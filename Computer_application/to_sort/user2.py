import sys
sys.path.append('../..')
from threading import *
import socket
import webbrowser


host = socket.gethostbyname(socket.gethostname())
port = 0
server = (socket.gethostbyname(socket.gethostname()), 51245)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
username = 'Вася'
s.sendto(('@' + username + " : join chat " + '\n').encode("utf-8"), server)

def receving(s):
    while True:
        try:
            data, addr = s.recvfrom(1024)
            data = data.decode('utf-8')
            print(data)
            if 'https://www.' in data:
                if yes_no := True:
                    webbrowser.open(data[data.index('[') + 1:data.index(']')])
        except:
            pass

def sending():
    try:
        message = 'Привет всем! Я Вася!'
        if message != '':
            s.sendto(('@' + username + ' : ' + message).encode('utf-8'), server)
    except:
        s.sendto(('@' + username + " : left chat " + '\n').encode("utf-8"), server)

thr1 = Thread(target=sending)
thr1.daemon = True
thr1.start()
thr1.join()

thr2 = Thread(target=receving, args=(s,))
thr2.daemon = True
thr2.start()
thr2.join()


