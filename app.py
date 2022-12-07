import json
import os

import requests
from flask import Flask, request

IS_SERVERLESS = bool(os.environ.get('SERVERLESS'))
print(IS_SERVERLESS)

app = Flask(__name__)



# 初始化上传临时目录

@app.route('/test', methods=['GET'])
def test():
    return 'test'


@app.route('/chat', methods=['POST'])
def chat():
    url = os.getenv('HANDLE_URL')
    requests.post(url, data=json.dumps(request.json))
    return 'success'


# 启动服务，监听 9000 端口，监听地址为 0.0.0.0
app.run(debug=IS_SERVERLESS != True, port=9000, host='0.0.0.0')
