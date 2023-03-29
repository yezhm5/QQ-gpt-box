import os
import sys

# bat
# if windows server
curPath = os.path.abspath(os.path.dirname(__file__))
bat_dir = os.path.join(curPath, "go-cqhttp")
bat_path = os.path.join(bat_dir, "go-cqhttp.bat")
bat_command = bat_path

# 重写bat程序，使可以直接在主环境运行
with open(bat_path, 'w') as f:
    text = "cd /d " + bat_dir + "\n" + 'start cmd /K "go-cqhttp.exe"'
    f.write(text)



base_url = 'http://127.0.0.1:5700'  # go-cqhttp发送端口


myqq = 123456       # 小QQ

# 需要回应的群组
group_list = []
# 需要回应的人
private_list = [654321]


