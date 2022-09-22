from flask import json
from service.SendMessage import feishu_send_message


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
        text = type[1]
        switcher = {
            '踏出的一小步': test,
            # '笑话': joke
            # '天气': getWeather,
            # '翻译': getTranslate,
            # '笑话': getJoke,
            # '菜谱': getCookbook,
            # '新闻': getNews,
            # '股票': getStock,
            # '快递': getExpress,
        }
        func = switcher.get(type, lambda x, y: {
            'text': '我不知道你在说什么'
        })
        # 调用方法
        message_card = func(user_id, user_name)
        # 返回成功响应
        feishu_send_message(message_card, message_id)
    print('success')
    return 'success'


def test(user_id, user_name):
    # 获取笑话
    content = '机器人的一大步'
    # 构造消息卡片
    message_card = {
        'text': f'<at user_id="{user_id}">{user_name}</at> {content}',
    }
    return message_card
