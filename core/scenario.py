from core.client import IRCClient

class Scenario:
    def __init__(self):
        self.clients = []

    def add_client(self, nick):
        c = IRCClient(nick)
        c.connect()
        c.register()
        self.clients.append(c)
        return c

    def join_all(self, channel):
        for c in self.clients:
            c.join(channel)

    def broadcast(self, sender, channel, msg):
        sender.privmsg(channel, msg)

    def cleanup(self):
        for c in self.clients:
            c.close()