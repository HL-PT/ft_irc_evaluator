import socket
import time
from config import HOST, PORT

def test_partial_packet():
    s = socket.socket()
    s.connect((HOST, PORT))

    s.send(b"NICK par")
    time.sleep(0.2)
    s.send(b"tial\r\n")

    s.send(b"USER partial 0 * :p\r\n")

    data = s.recv(4096).decode()

    assert "001" in data, "❌ partial packet failed"

    s.close()
    print("✅ partial packet passed")