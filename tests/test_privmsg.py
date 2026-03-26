from core.client import IRCClient

def test_private_message():
    c1 = IRCClient("sender")
    c2 = IRCClient("receiver")

    c1.connect()
    c2.connect()

    c1.register()
    c2.register()

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
	
    c1.privmsg("#chan", "hi all")

    resp = c2.recv_all()

    assert "hi all" in resp, "❌ Channel message failed"

    c1.close()
    c2.close()
    print("✅ test_channel_message passed")