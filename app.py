import json
import os
from concurrent.futures import ThreadPoolExecutor

from flask import Flask, jsonify, render_template, request, url_for, send_from_directory
from service import ContentDistributor
from werkzeug.utils import secure_filename

IS_SERVERLESS = bool(os.environ.get('SERVERLESS'))
print(IS_SERVERLESS)

app = Flask(__name__)


executor = ThreadPoolExecutor(max_workers=1)


# 初始化上传临时目录

@app.route('/test', methods=['GET'])
def test():
    return 'test'


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json['event']
    # 异步处理消息
    executor.submit(ContentDistributor.distributeContent(data))
    return 'success'


# 启动服务，监听 9000 端口，监听地址为 0.0.0.0
app.run(debug=IS_SERVERLESS != True, port=9000, host='0.0.0.0')
