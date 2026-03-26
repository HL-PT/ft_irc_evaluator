from core.client import IRCClient
from core.parser import parse_irc_message
from core.assertor import assert_reply

def test_full_registration():
    c = IRCClient("auth1")
    c.connect()
    c.register()

    msgs = parse_irc_message(c.recv_all())

    assert_reply(msgs, "001")  # welcome
    assert_reply(msgs, "002")
    assert_reply(msgs, "003")

    c.close()
    print("✅ auth full passed")

def test_basic_registration():
    c = IRCClient("user1")
    c.connect()
    c.register()

    resp = c.recv_all()

    assert "001" in resp, "❌ No welcome message (001)"
    c.close()
    print("✅ test_basic_registration passed")


def test_duplicate_nick():
    c1 = IRCClient("dup")
    c1.connect()
    c1.register()

    c2 = IRCClient("dup")
    c2.connect()
    c2.register()

    resp = c2.recv_all()

    assert "433" in resp, "❌ Duplicate nick not rejected"

    c1.close()
    c2.close()
    print("✅ test_duplicate_nick passed")