from core.scenario import Scenario
from core.parser import parse_irc_message

def test_invite_only_channel():
    s = Scenario()

    op = s.add_client("op")
    u = s.add_client("u")

    op.join("#i")
    op.send("MODE #i +i")

    op.send("INVITE u #i")

    msgs = parse_irc_message(u.recv_all())

    found = any(m["command"] == "INVITE" for m in msgs)
    assert found, "❌ invite failed"

    s.cleanup()
    print("✅ invite passed")