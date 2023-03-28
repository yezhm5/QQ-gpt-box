# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
from typing import List
import json
import sys
import time
import openai

import openai
import requests
from requests.structures import CaseInsensitiveDict
import os


os.environ["HTTP_PROXY"] = "http://127.0.0.1:10809"
os.environ["HTTPS_PROXY"] = "http://127.0.0.1:10809"
class ChatGPT_use:

    def __init__(self, api_key: str, messages: List = None):
        openai.api_key = api_key
        
        if messages: 
            self.messages = messages   
        else:
            self.messages = [
                # {"role": "system", "content": "You are a helpful assistant."},               
                {"role":"system", "content": "你是一个什么问题都会的，什么难题都能解决的人类助手。"},
                {"role": "user", "content": "你好,可以简单介绍一下你的功能和作用吗？接下来我要随意问你一些问题，你会给出合理精确有用的解答。"},
            ]  
    def ask_chat_gpt(self) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        response_content = response['choices'][0]['message']['content']
        return response_content
    
def ChatBOT(self):
    print("Initializing ChatGPT services...")
    self.ask_chat_gpt()
    print("success!")
    while True:
        # time.sleep(0.5)
        try:
            prompt = input("Q:")
            if prompt =="exit_chatgpt":
                print("Exit success!Enjoy your chat.")
                return 
            print("AI is thinking...")
            self.messages.append({"role": "user", "content": f"Q:{prompt}"})
            response_content = self.ask_chat_gpt()
            self.messages.append({"role": "assistant", "content": f"{response_content}"})
            print(response_content)
        except openai.error.RateLimitError:
            para_input = {"name": "Chatbot","prompt":prompt,"messages":self.messages}
            print(" That model is currently overloaded with other requests. You can retry your request, or contact us through our help center at help.openai.com if the error persists")
            return para_input
        except Exception as e:
            para_input = {"name": "Chatbot","prompt":prompt,"messages":self.messages}
            print(e)
            time.sleep(10)

def QQ_box(self,prompt):

    self.messages.append({"role": "user", "content": f"Q:{prompt}"})
    response_content = self.ask_chat_gpt()
    self.messages.append({"role": "assistant", "content": f"{response_content}"})
    if len(self.messages)>10:
        self.meassages = [
                # {"role": "system", "content": "You are a helpful assistant."},               
                {"role":"system", "content": "你是一个什么问题都会的，什么难题都能解决的人类助手。"},
                {"role": "user", "content": "你好,可以简单介绍一下你的功能和作用吗？接下来我要随意问你一些问题，你会给出合理精确有用的解答。"},
            ]  
    return response_content


# api_key = "sk-M...."
from apikey import api_key
Chat_GPT = ChatGPT_use(api_key=api_key)
#test
 
response = QQ_box(Chat_GPT,"请问什么是酱油")
print(response)

ChatBOT(Chat_GPT)   