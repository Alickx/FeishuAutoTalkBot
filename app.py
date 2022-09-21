from flask import Flask, jsonify, render_template
from flask.flask import request

app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():
    challenge = request.json.get("CHALLENGE")
    return challenge

# HTTP 直通函数由于是基于 docker 镜像运行，所以必须监听地址为 0.0.0.0，并且端口为 9000
app.run(host = '0.0.0.0', port = 9000)
