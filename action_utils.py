
import go_cqhttp_api
import settings
from ChatGPT_chat_demo import ChatGPT_use,QQ_box
from apikey import api_key

action_status = {}

CQ_at_me = f'[CQ:at,qq={settings.myqq}] '
def at_me(message):
    if CQ_at_me in message:
        return True
    else:
        return False



def action_follow_rec(data):
    Chatbot = ChatGPT_use(api_key=api_key)
    message_type = data.get('message_type', None)
    if message_type == 'group':
        sender_info = data.get('sender', None)
        group_id = data.get('group_id', None)
        message = data.get('message', None)

        if at_me(message) and group_id in settings.group_list:
            # 群里被@到的操作

            # 获取chatgpt返回
            response = ""
            # 发送到该群
            go_cqhttp_api.send_group_msg(group_id, response)
            pass

    elif message_type == 'private':
        if data["sender"]["user_id"] in settings.private_list:
            user_id = data['sender']['user_id']
            nickname = data['sender']['nickname']
            msg = data['message']

            # 获取chatgpt返回
            response = QQ_box(Chatbot,msg)
            # 发送给该用户
            go_cqhttp_api.send_private_msg(user_id, response)
            pass



