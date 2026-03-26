import tests.test_auth as test_auth
import tests.test_channel as test_channel
import tests.test_privmsg as test_privmsg

def run_all():
    print("🚀 Running ft_irc tests...\n")

    test_auth.test_basic_registration()
    test_auth.test_duplicate_nick()

    test_channel.test_join_channel()
    test_channel.test_multi_join()

    test_privmsg.test_private_message()
    test_privmsg.test_channel_message()

    print("\n🎉 All tests passed!")

if __name__ == "__main__":
    run_all()