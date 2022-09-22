import json
import os
from flask import Flask, jsonify, render_template, request, url_for, send_from_directory
from service import ContentDistributor
from werkzeug.utils import secure_filename

IS_SERVERLESS = bool(os.environ.get('SERVERLESS'))
print(IS_SERVERLESS)

app = Flask(__name__)


# 初始化上传临时目录

@app.route('/test', methods=['GET'])
def test():
    return 'test'


@app.route('/chat', methods=['POST'])
def chat():
    challenge = request.json['challenge']
    return jsonify({'challenge': challenge})
    # data = request.json['event']
    # return ContentDistributor.distributeContent(data)


# 启动服务，监听 9000 端口，监听地址为 0.0.0.0
app.run(debug=IS_SERVERLESS != True, port=9000, host='0.0.0.0')
