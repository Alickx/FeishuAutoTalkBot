import os
from concurrent.futures import ThreadPoolExecutor

import openai
from flask import json
from service.SendMessage import feishu_send_message

executor = ThreadPoolExecutor()


def distributeContent(data):
    # 1. 获取消息文本
    user_id = data['sender']['sender_id']['user_id']
    user_name = data['message']['mentions'][0]['name']
    textJson = data['message']['content']
    message_id = data['message']['message_id']
    text = json.loads(textJson)['text']

    print(f'收到消息: {text}')

    # 2. 根据消息类型，调用不同的分发方法
    # 解析文本，获取消息类型
    type = text.split(' ')
    # 如果长度为 1，说明只有一个命令，没有参数
    if len(type) == 1:
        card = {
            'text': '我不知道你在说什么'
        }
        feishu_send_message(card, message_id)
    else:
        instructions = type[1]
        content = getAiComment(instructions)
        # 构造消息卡片
        message_card = {
            'text': f'<at user_id="{user_id}">{user_name}</at> {content}',
        }
        # 返回成功响应
        feishu_send_message(message_card, message_id)
    print('success')


# 调用接口获取回复的消息
def getAiComment(text):


    openai.api_key = os.getenv('OPENAI_API_KEY')

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{text}",
        temperature=0.7,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    text = response["choices"][0]["text"]
    # unicode转中文
    text = text.encode('utf-8').decode('utf-8')
    return text


def async_distributeContent(data):
    executor.submit(distributeContent(data))
