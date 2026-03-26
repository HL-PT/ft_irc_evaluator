def assert_reply(messages, code):
    for msg in messages:
        if msg["command"] == code:
            return True
    raise AssertionError(f"❌ Missing reply {code}")


def assert_privmsg(messages, sender, content):
    for msg in messages:
        if msg["command"] == "PRIVMSG":
            if msg["prefix"].startswith(sender) and msg["trailing"] == content:
                return True
    raise AssertionError("❌ PRIVMSG mismatch")


def assert_join(messages, nick, channel):
    for msg in messages:
        if msg["command"] == "JOIN":
            if nick in msg["prefix"] and msg["params"][0] == channel:
                return True
    raise AssertionError("❌ JOIN failed")