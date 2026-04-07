import socket
import time
from config import HOST, PORT, BUFFER_SIZE, TIMEOUT, PASSWORD

class IRCClient:
    def __init__(self, nick):
        self.nick = nick
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(TIMEOUT)
        self.tcp_nodelay = True

    def connect(self):
        self.sock.connect((HOST, PORT))

    def send(self, msg):
        full = msg + "\r\n"
        self.sock.send(full.encode())

    def recv_all(self):
        data = ""
        retries = 0
        max_retries = 5
        
        while retries < max_retries:
            try:
                chunk = self.sock.recv(BUFFER_SIZE).decode()
                if chunk:
                    data += chunk
                    retries = 0  # Reset retries on successful recv
                else:
                    break
            except socket.timeout:
                if data:  # If we have data, we're done
                    break
                retries += 1
                time.sleep(0.1)  # Wait a bit before retrying
            except:
                break
        
        return data

    def register(self):
        self.send(f"PASS {PASSWORD}")
        self.send(f"NICK {self.nick}")
        self.send(f"USER {self.nick} 0 * :{self.nick}")

    def join(self, channel):
        self.send(f"JOIN {channel}")

    def privmsg(self, target, msg):
        self.send(f"PRIVMSG {target} :{msg}")

    def quit(self):
        self.send("QUIT")

    def close(self):
        self.sock.close()

    def debug_recv(self):
        data = self.recv_all()
        print(f"[{self.nick} recv]:\n{data}")
        return data

    def connection_alive(self):
        try:
            self.sock.send(b"PING\r\n")
            return True
        except:
            return False