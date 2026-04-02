import time
from core.scenario import Scenario
from core.parser import parse_irc_message

def test_invite():
    test_invite_chanel_not_exist()
    test_invite_nick_not_exist()
    test_invite_not_operator()
    test_invite_only_channel()

def test_invite_chanel_not_exist():
    s = Scenario()

    op = s.add_client("op")
    u = s.add_client("u")
    time.sleep(0.1)  # Ensure clients are connected
    op.send("INVITE u #nonexistent")

    msgs = parse_irc_message(op.recv_all())

    # print(msgs)

    found = any(m["command"] == "403" for m in msgs)
    assert found, "❌ invite non-existent channel failed"

    s.cleanup()
    print("✅ invite non-existent channel passed")

def test_invite_nick_not_exist():
    s = Scenario()

    op = s.add_client("op")
    time.sleep(0.1)  # Ensure clients are connected
    op.join("#channelNickNotExist")
    op.send("MODE #channelNickNotExist +i")

    op.send("INVITE nonuser #channelNickNotExist")

    msgs = parse_irc_message(op.recv_all())

    # print(msgs)

    found = any(m["command"] == "401" for m in msgs)
    assert found, "❌ invite non-existent user failed"

    s.cleanup()
    print("✅ invite non-existent user passed")

def test_invite_not_operator():
    s = Scenario()

    op = s.add_client("op")
    u = s.add_client("u")
    time.sleep(0.1)  # Ensure clients are connected
    op.join("#i")
    op.send("MODE #i +i")

    u.send("INVITE u #i")

    msgs = parse_irc_message(u.recv_all())

    # print(msgs)

    found = any(m["command"] == "482" for m in msgs)
    assert found, "❌ invite by non-operator failed"

    s.cleanup()
    print("✅ invite by non-operator passed")

def test_invite_only_channel():
    s = Scenario()

    op = s.add_client("op")
    u = s.add_client("u")
    time.sleep(0.1)  # Ensure clients are connected
    op.join("#iamop")
    op.send("MODE #iamop +i")

    op.send("INVITE u #iamop")

    msgs = parse_irc_message(u.recv_all())

    # print(msgs)

    found = any(m["command"] == "INVITE" for m in msgs)
    assert found, "❌ invite failed"

    s.cleanup()
    print("✅ invite passed")