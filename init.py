from flask import Flask, request

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    return request.json.get('challenge')


if __name__ == '__main__':
    app.run()
