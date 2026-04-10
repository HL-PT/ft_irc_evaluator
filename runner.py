import tests.test_auth as auth
import tests.test_broadcast as broadcast
import tests.test_channel as channel
import tests.test_disconnect as disc
import tests.test_invite as invite
import tests.test_mode as mode
import tests.test_operator as op
import tests.test_parser_edge as edge
import tests.test_privmsg as privmsg
import tests.test_reconnect as reconnect
import tests.test_topic as topic
import tests.test_who as who


def run():
    print("🚀 IRC EVALUATION TEST START\n")

    # auth.test_full_registration()
    # auth.test_basic_registration()
    # auth.test_duplicate_nick()

    # broadcast.test_broadcast_consistency()

    # channel.test_join_channel()
    # channel.test_multi_join()

    # disc.test_disconnect_cleanup()
    # privmsg.test_private_message()
    # privmsg.test_channel_message()
    # privmsg.test_private_bigmessage()
    # privmsg.test_private_bigmessage2()
    # invite.test_invite()
    # mode.test_operator_mode()


    op.test_kick()

    # edge.test_partial_packet()

    # reconnect.test_reconnect()

    # topic.test_topic()

    # who.test_who()

    print("\n🎯 ALL CORE TESTS TESTED")

if __name__ == "__main__":
    run()