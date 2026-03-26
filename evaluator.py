from evaluation.auth_eval import eval_auth
from evaluation.channel_eval import eval_channel
from evaluation.mode_eval import eval_mode
from evaluation.disconnect_eval import eval_disconnect

from report.logger import print_report

def run():
    eval_auth()
    eval_channel()
    eval_mode()
    eval_disconnect()

    print_report()

if __name__ == "__main__":
    run()