from core.client import IRCClient
from time import sleep

def test_private_message():
    c1 = IRCClient("sender")
    c2 = IRCClient("receiver")

    c1.connect()
    c2.connect()

    c1.register()
    c2.register()

    sleep(0.5)  # Wait for registration to process
    c1.privmsg("receiver", "hello")

    resp = c2.recv_all()

    assert "hello" in resp, "❌ PRIVMSG not received"

    c1.close()
    c2.close()
    print("✅ test_private_message passed")


def test_channel_message():
    c1 = IRCClient("c1")
    c2 = IRCClient("c2")

    c1.connect()
    c2.connect()

    c1.register()
    c2.register()

    c1.join("#chan")
    c2.join("#chan")
	
    sleep(0.5)  # Wait for join to process

    for index in range(12):
        c1.privmsg("#chan", "hi all "+str(index))
        sleep(0.01)  # Small delay to ensure messages are processed

    c1.privmsg("#chan", "hi all")

    resp = c2.recv_all()
    assert resp.count("hi all") == 13, "❌ Channel message failed"

    c1.close()
    c2.close()
    print("✅ test_channel_message passed")

def test_private_bigmessage():
    c1 = IRCClient("sender")
    c2 = IRCClient("receiver")

    c1.connect()
    c2.connect()

    c1.register()
    c2.register()

    sleep(0.5)  # Wait for registration to process
    c1.privmsg("receiver", "0123456789"*10000)

    sleep(0.5)    
    assert c1.connection_alive() is False, "❌ PRIVMSG not received"

    c1.close()
    c2.close()
    print("✅ test_private_bigmessage passed")

def test_private_bigmessage2():
    c1 = IRCClient("sender")
    c2 = IRCClient("receiver")

    c1.connect()
    c2.connect()

    c1.register()
    c2.register()

    c1.join("#chan")
    c2.join("#chan")

    sleep(0.5)  # Wait for registration to process
    for index in range(1000):
        c1.privmsg("#chan", str(index)+":0123456789"*51)

    resp = c2.recv_all()
    respc1 = c1.recv_all()

    assert c1.connection_alive() is True, "❌ PRIVMSG not received"

    c1.close()
    c2.close()
    print("✅ test_private_bigmessage passed")