from core.client import IRCClient
from core.parser import parse_irc_message

def test_kick():
    op = IRCClient("op")
    u = IRCClient("victim")

    op.connect()
    u.connect()

    op.register()
    u.register()

    op.join("#room")
    u.join("#room")

    op.send("MODE #room +o op")
    op.send("KICK #room victim :bye")

    msgs = parse_irc_message(u.recv_all())

    found = any(m["command"] == "KICK" for m in msgs)
    assert found, "❌ KICK failed"

    op.close()
    u.close()
    print("✅ kick passed")