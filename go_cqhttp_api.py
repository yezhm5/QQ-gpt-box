import requests
import settings
import os

def restart_cqhttp():
    url = settings.base_url + '/set_restart'
    ans = requests.get(url, data={'delay':2000})
    return ans

def send_private_msg(user_id, msg):
    data = {"user_id": user_id, "message": msg}
    # print(settings.base_url + "/send_private_msg")
    session = requests.Session()
    session.trust_env = False
    ans = session.post(settings.base_url + "/send_private_msg", data=data)
    # ans = requests.post(settings.base_url + "/send_private_msg", data=data)
    print(ans.json())

def send_group_msg(group_id, msg):
    data = {"group_id": group_id, "message": msg}
    session = requests.Session()
    session.trust_env = False
    ans = session.post(settings.base_url + "/send_group_msg", data=data)
    # ans = requests.post(settings.base_url + "/send_group_msg", data=data)
    # print(ans.json())


def send_pic_2_group(group_id, pic_path):
    # 发送本地图片
    msg = f"[CQ:image,file=file:///{pic_path}]"
    send_group_msg(group_id, msg)

def send_pic_2_group2(group_id, url):
    # 发送网络图片
    msg = f"[CQ:image,url={url}]"
    send_group_msg(group_id, msg)


def get_group_info(group_id):
    data = {"group_id": group_id, 'no_cache':True}
    url = settings.base_url + '/get_group_info'
    ans = requests.post(url, data = data)
    return ans.json()

def get_group_headimg(group_id):
    # 获取群图片 https://p.qlogo.cn/gh/{group_id}/{group_id}/100
    save_path = os.path.join(settings.group_headimg_dir, str(group_id)+'.jpg')
    if os.path.exists(save_path):
        return save_path
    url = f'https://p.qlogo.cn/gh/{group_id}/{group_id}/100'
    r = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(r.content)
    return save_path



def get_qq_headimg(user_id):
    save_path = os.path.join(settings.user_headimg_dir, str(user_id) + '.jpg')
    if os.path.exists(save_path):
        return save_path
    url = f'https://q2.qlogo.cn/headimg_dl?dst_uin={user_id}&spec=100'
    r = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(r.content)
    return save_path

def get_msg(message_id):
    url = settings.base_url + '/get_msg'
    r = requests.post(url, data={'message_id': message_id})
    print(r.json())

def get_group_member_info(group_id, user_id, no_cache = True):
    url = settings.base_url + '/get_group_member_info'
    r = requests.post(url, data={'group_id': group_id, 'user_id': user_id, 'no_cache':no_cache})
    print(r.json())
    return r.json()


if __name__ == '__main__':
    pass
