from core.scenario import Scenario
import time

def test_broadcast_consistency():
    s = Scenario()

    users = [s.add_client(f"u{i}") for i in range(5)]

    s.join_all("#b")
    
    # # Clear socket buffers after join responses
    # for u in users:
    #     u.recv_all()
    
    time.sleep(0.1)

    users[0].privmsg("#b", "hello")
    time.sleep(0.5)  # Give server time to process and broadcast

    for u in users[1:]:
        data = u.recv_all()
        print(f"[{u.nick} recv]:\n{data}")
        assert "hello" in data, "❌ broadcast lost"

    s.cleanup()
    print("✅ broadcast consistency passed")