from core.client import IRCClient
from core.parser import parse_irc_message
from report.scorer import set_result

def eval_channel():
    c = IRCClient("c1")
    c.connect()
    c.register()

    c.join("#eval")

    msgs = parse_irc_message(c.recv_all())

    codes = [m["command"] for m in msgs]

    if "353" in codes and "366" in codes:
        set_result("CHANNEL", "PASS")
    elif "JOIN" in codes:
        set_result("CHANNEL", "PARTIAL", "Missing RPL_NAMREPLY (353)")
    else:
        set_result("CHANNEL", "FAIL", "JOIN failed")

    c.close()