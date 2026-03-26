from core.client import IRCClient

def test_join_channel():
    c = IRCClient("user_join")
    c.connect()
    c.register()

    c.join("#test")
    resp = c.recv_all()

    assert "JOIN" in resp, "❌ JOIN not working"

    c.close()
    print("✅ test_join_channel passed")


def test_multi_join():
    c1 = IRCClient("u1")
    c2 = IRCClient("u2")

    c1.connect()
    c2.connect()

    c1.register()
    c2.register()

    c1.join("#room")
    c2.join("#room")

    resp = c1.recv_all()

    assert "u2" in resp, "❌ Second user not visible in channel"

    c1.close()
    c2.close()
    print("✅ test_multi_join passed")