from core.client import IRCClient
from core.parser import parse_irc_message

def test_who():
    c = IRCClient("who1")
    c.connect()
    c.register()

    c.join("#who")
    c.send("WHO #who")

    msgs = parse_irc_message(c.recv_all())

    found = any(m["command"] == "352" for m in msgs)
    assert found, "❌ WHO reply missing (352)"

    c.close()
    print("✅ WHO passed")