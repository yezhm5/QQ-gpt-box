# QQ-ChatBot based on ChatGPT & ChatGLM
    这是一个用于构建QQ版ChatGPT的项目，当前项目需要使用你的openai账号生成APIKEY，以及一点点魔法，简单实现QQ自动抓取信息，以及用Chat机器人回复的小程序。
    此版本为linux分支，若要查看windows版本，请转到分支 QQ_bot_windows_v1.0


# 配置go-cqhttp
详细教程见[go-cqhttp教程](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B)
- 进入go-cqhttp文件夹，解压go-cqhttp_linux_amd64.tar.gz，修改 go-cqhttp 文件执行权限，运行 go-cqhttp
```
cd go-cqhttp
chmod 777 go-cqhttp
./go-cqhttp
```
- 通讯方式选择0
- 生成的config.yml中，4、5行填上QQ账号和密码
- config.yml中104行的url: 'http://127.0.0.1:8080' 为本项目的server地址，如果更改过flask的host或port，请同时修改此处
- 重新执行go-cqhttp程序完成验证后，可以退出

# 配置项目
   - 如果在国内运行，需要开启VPN，VPN的端口配置在ChatGPT_chat_demo.py的9、10行中
   - 要创建apikey.py
```
# apikey.py
api_key = ""    # 加上自己的chatgpt的key
```

# 运行项目
- python server.py 运行项目即可
- 项目listener会自动启动和监听go-cqhttp程序，若长时间未收到会重启


# 运行截图
![GPT回复图片](img/001.jpg "gpt_chat")
