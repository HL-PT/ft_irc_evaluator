from core.scenario import Scenario
from core.parser import parse_irc_message

def test_topic():
    s = Scenario()

    c1 = s.add_client("t1")
    c2 = s.add_client("t2")

    s.join_all("#t")

    c1.send("TOPIC #t :hello world")

    msgs = parse_irc_message(c2.recv_all())

    found = any(m["command"] == "TOPIC" for m in msgs)
    assert found, "❌ topic not broadcast"

    s.cleanup()
    print("✅ topic passed")