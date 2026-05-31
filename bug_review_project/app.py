from flask import Flask, request
from auth import login
from calculator import divide
from api_handler import process_user

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')

    # 未校验空值
    return login(username, password)

@app.route('/divide')
def division():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))

    # 未处理除零
    return str(divide(a, b))

@app.route('/user')
def user_process():
    data = request.args.get('data')

    # XSS风险
    return process_user(data)

if __name__ == '__main__':
    app.run(debug=True)