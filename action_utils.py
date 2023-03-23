
from go_cqhttp_api import *


action_status = {}

CQ_at_me = f'[CQ:at,qq={settings.myqq}] '
def at_me(message):
    if CQ_at_me in message:
        return True
    else:
        return False



def action_follow_rec(data):
    message_type = data.get('message_type', None)
    if message_type == 'group':
        sender_info = data.get('sender', None)
        group_id = data.get('group_id', None)
        message = data.get('message', None)

        if at_me(message) and group_id in settings.group_list:
            # 群里被@到的操作
            pass

    elif message_type == 'private':
        if data["sender"]["user_id"] in settings.private_list:
            nickname = data['sender']['nickname']
            msg = data['message']
            report_master(None, nickname, msg)
            pass



