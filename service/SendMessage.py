import os
import uuid

import requests


def feishu_send_message(content, message_id):
    token = get_token()
    url = f'https://open.feishu.cn/open-apis/im/v1/messages/{message_id}/reply'
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Bearer ' + token
    }

    data = {
        'content': f'{content}',
        'msg_type': 'text',
        'uuid': get_uuid()
    }

    res = requests.post(url=url, headers=headers, json=data)
    print(res.json())
    return res.json()


def get_token():
    feishu_app_id = os.environ['FEISHU_APP_ID']
    feishu_app_secret = os.environ['FEISHU_APP_SECRET']

    url = f'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal?app_id={feishu_app_id}&app_secret={feishu_app_secret}'
    res = requests.get(url=url)
    token = res.json()
    token_text = token['tenant_access_token']
    return token_text


def get_uuid():
    return str(uuid.uuid1())
