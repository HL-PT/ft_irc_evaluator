from core.client import IRCClient
from core.parser import parse_irc_message
from report.scorer import set_result

def eval_auth():
    c = IRCClient("eval_auth")
    c.connect()
    c.register()

    msgs = parse_irc_message(c.recv_all())

    codes = [m["command"] for m in msgs]

    if "001" in codes:
        set_result("AUTH", "PASS")
    else:
        set_result("AUTH", "FAIL", "Missing 001 welcome")

    c.close()