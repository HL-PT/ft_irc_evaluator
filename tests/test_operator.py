from core.client import IRCClient
from core.parser import parse_irc_message
import time

def test_kick():
    op = IRCClient("op")
    u = IRCClient("victim")

    op.connect()
    u.connect()

    op.register()
    u.register()

    op.join("#room")
    u.join("#room")

    time.sleep(0.1)  # Wait for join to process
    op.send("MODE #room +o op")
    op.send("KICK #room victim :bye")

    time.sleep(0.1)  # Wait for kick to process
    msgs = parse_irc_message(u.recv_all())
    u.debug_recv()  # Should receive the kick message without error

    # op.debug_recv()  # Should receive the kick message without error

    found = any(m["command"] == "KICK" for m in msgs)
    assert found, "❌ KICK failed"

    op.close()
    u.close()
    print("✅ kick passed")