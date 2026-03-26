import socket
import time
from config import HOST, PORT

def fuzz():
    s = socket.socket()
    s.connect((HOST, PORT))

    payloads = [
        b"NICK a\r\nUSER a 0 * :a\r\n",
        b"JOIN #a\r\nPRIV",
        b"MSG #a :split\r\n",
    ]

    for p in payloads:
        s.send(p)
        time.sleep(0.1)

    print(s.recv(4096).decode())
    s.close()