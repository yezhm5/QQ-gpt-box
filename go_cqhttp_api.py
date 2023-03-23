import requests
import settings
import os

def restart_cqhttp():
    url = settings.base_url + '/set_restart'
    ans = requests.get(url, data={'delay':2000})
    return ans

def send_private_msg(user_id, msg):
    data = {"user_id": user_id, "message": msg}
    ans=  requests.post("http://127.0.0.1:5710/send_private_msg", data=data)


def send_group_msg(group_id, msg):
    data = {"group_id": group_id, "message": msg}
    ans = requests.post("http://127.0.0.1:5710/send_group_msg", data=data)
    # print(ans.json())


def send_setu_2_group(group_id, pic_path):
    msg = f"[CQ:image,file=file:///{pic_path}]"
    send_group_msg(group_id, msg)

def send_setu_2_group2(group_id, url):
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

def get_msg(message_id = 1931600985):
    url = settings.base_url + '/get_msg'
    r = requests.post(url, data={'message_id': message_id})
    print(r.json())

def get_group_member_info(group_id = 260119646, user_id = 43312024, no_cache = True):
    url = settings.base_url + '/get_group_member_info'
    r = requests.post(url, data={'group_id': group_id, 'user_id': user_id, 'no_cache':no_cache})
    print(r.json())
    return r.json()


if __name__ == '__main__':
    # send_setu_2_group(1004183903, r'C:/Users/43312/Pictures/timg1.jpg')
    # send_setu_2_group2(1004183903, "http://img95.699pic.com/photo/40094/7630.jpg_wh300.jpg")
    # send_private_msg(43312024, '主人你好')
    # data = get_group_info(15938891)
    # print(data)
    ans = restart_cqhttp()
    print(ans)
    # ans = get_group_member_info(user_id=1792312584)
