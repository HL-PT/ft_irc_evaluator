from core.client import IRCClient

def stress_test(n=100):
    clients = []

    for i in range(n):
        c = IRCClient(f"s{i}")
        c.connect()
        c.register()
        c.join("#stress")
        clients.append(c)

    clients[0].privmsg("#stress", "boom")

    for c in clients:
        c.recv_all()

    print(f"✅ stress test with {n} clients done")

    for c in clients:
        c.close()