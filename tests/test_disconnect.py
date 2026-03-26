from core.client import IRCClient
import time

def test_disconnect_cleanup():
    c1 = IRCClient("d1")
    c2 = IRCClient("d2")

    c1.connect()
    c2.connect()

    c1.register()
    c2.register()

    c1.join("#room")
    c2.join("#room")

    c2.close()  # 模拟 crash

    time.sleep(1)

    c1.recv_all()  # Clear any pending messages
    c1.send("WHO #room")
    resp = c1.recv_all()
    print(f"[{c1.nick} recv]:\n{resp}")
    assert "d2" not in resp, "❌ disconnected user still present"

    c1.close()
    print("✅ disconnect cleanup passed")