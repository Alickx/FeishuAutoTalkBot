from flask import json
from service.SendMessage import feishu_send_message


def distributeContent(data):
    # 1. 获取消息文本
    user_id = data['sender']['sender_id']['user_id']
    textJson = data['message']['content']
    message_id = data['message']['message_id']
    text = json.loads(textJson)['text']

    print(f'收到消息: {text}')

    # 2. 根据消息类型，调用不同的分发方法
    # 解析文本，获取消息类型
    type = text.split(' ')[1]
    switcher = {
        '笑话': joke
        # '天气': getWeather,
        # '翻译': getTranslate,
        # '笑话': getJoke,
        # '菜谱': getCookbook,
        # '新闻': getNews,
        # '股票': getStock,
        # '快递': getExpress,
    }
    func = switcher.get(type, lambda x: {
        'text': '我不知道你在说什么'
    })
    # 调用方法
    message_card = func(user_id)
    # 返回成功响应
    feishu_send_message(message_card, message_id)
    print('success')
    return 'success'


def joke(user_id):
    # 获取笑话
    content = '我这个就是个笑话'
    # 构造消息卡片
    message_card = {
        'text': f'<at user_id="{user_id}"> {content}',
    }
    return message_card
