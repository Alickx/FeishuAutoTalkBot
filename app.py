from flask import Flask, jsonify, render_template
from flask.flask import request

app = Flask(__name__)


@app.route("/chat")
def chat():
    challenge = request.args.get("challenge")
    return challenge

# HTTP 直通函数由于是基于 docker 镜像运行，所以必须监听地址为 0.0.0.0，并且端口为 9000
app.run(host = '0.0.0.0', port = 9000)
