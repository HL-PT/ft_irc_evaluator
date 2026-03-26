from core.client import IRCClient
import time

def test_reconnect():
    c1 = IRCClient("re")
    c1.connect()
    c1.register()

    c1.close()

    time.sleep(1)

    c2 = IRCClient("re")
    c2.connect()
    c2.register()

    resp = c2.recv_all()

    assert "001" in resp, "❌ reconnect failed"

    c2.close()
    print("✅ reconnect passed")