from core.scenario import Scenario
from core.parser import parse_irc_message

def test_operator_mode():
    s = Scenario()

    op = s.add_client("op")
    u = s.add_client("user")

    op.join("#room")
    u.join("#room")

    op.send("MODE #room +o op")

    op.send("MODE #room -o op")
    op.send("KICK #room user :fail")

    msgs = parse_irc_message(u.recv_all())

    assert "482" in op.recv_all(), "❌ operator mode failed"
    
    assert not any(m["command"] == "KICK" for m in msgs), \
        "❌ non-operator could kick"

    s.cleanup()
    print("✅ mode operator passed")