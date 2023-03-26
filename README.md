# QQ-ChatBot based on ChatGPT & ChatGLM
    这是一个用于构建QQ版ChatGPT的项目，当前项目需要使用你的openai账号生成APIKEY，以及一点点魔法，简单实现QQ自动抓取信息，以及用Chat机器人回复的小程序。


# 配置go-cqhttp
详细教程见[go-cqhttp教程](https://docs.go-cqhttp.org/guide/quick_start.html#%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B)
- 首先先下载对应版本的go-cqhttp 安装并生成config.yml文件和device.json文件，协议选择023。 
- 进入go-cqhttp文件夹，打开config.yml，按照教程修改，在第4行配置好QQ账号后退出
- 点击go-cqhttp.bat，完成扫码登录等操作后退出

# 运行项目
- python server.py 运行项目即可
- 项目listener会自动监听go-cqhttp程序，若长时间未收到会重启



