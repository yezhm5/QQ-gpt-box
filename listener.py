import time
import go_cqhttp_api
import settings
import os

os.system(settings.bat_path) # 启动程序
listen_info = {"last_time":time.time()}

def update_last_time():
    listen_info['last_time'] = time.time()

def restart_judge():
    # 长时间未收到消息，判断为断连，重启程序
    last_time = listen_info['last_time']
    if time.time() - last_time > 20*60:
        os.system(r'taskkill /f /t /im go-cqhttp.exe')
        os.system(r'taskkill /f /t /im cmd.exe')
        os.system(f'{settings.bat_path}')
        listen_info['last_time'] = time.time()