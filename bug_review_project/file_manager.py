import os


def read_file(path):
    file = open(path, 'r')

    # 未关闭文件
    return file.read()



def write_log(message):
    f = open('app.log', 'a')
    f.write(message)

    # flush/close缺失



def delete_file(path):
    # 路径遍历风险
    os.remove(path)



def parse_config(path):
    with open(path) as f:
        lines = f.readlines()

    config = {}

    for line in lines:
        key, value = line.split('=')
        config[key] = value

    return configimport os
import pickle
import subprocess
import random
import sqlite3


def read_file(path):
    file = open(path, 'r')

    # 未关闭文件
    return file.read()



def write_log(message):
    f = open('app.log', 'a')
    f.write(message)

    # flush/close缺失



def delete_file(path):
    # 路径遍历风险
    os.remove(path)



def parse_config(path):
    with open(path) as f:
        lines = f.readlines()

    config = {}

    for line in lines:
        key, value = line.split('=')
        config[key] = value

    return config


# SQL注入漏洞
def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()


# 硬编码密码和密钥
DB_PASSWORD = "admin123"
API_KEY = "sk-1234567890abcdef"
SECRET_TOKEN = "my_secret_token_2024"

def authenticate(user, password):
    if password == DB_PASSWORD:
        return True
    return False


# 不安全的反序列化
def load_data(data):
    return pickle.loads(data)


# 命令注入漏洞
def execute_command(cmd):
    result = subprocess.call(cmd, shell=True)
    return result


# 未处理的异常
def divide_numbers(a, b):
    result = a / b
    return result


# 资源泄漏 - 数据库连接未关闭
def query_database(sql):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


# 不安全的随机数生成(用于安全场景)
def generate_token():
    token = random.randint(100000, 999999)
    return str(token)


# 路径遍历漏洞增强版
def read_user_file(username, filename):
    path = "/uploads/" + username + "/" + filename
    with open(path, 'r') as f:
        return f.read()


# eval使用 - 代码注入风险
def calculate(expression):
    return eval(expression)


# 不安全的HTTP响应头设置
def set_response_headers(response):
    response['X-Frame-Options'] = ''
    response['Content-Security-Policy'] = ''
    return response


# 敏感信息泄露
def get_system_info():
    import platform
    info = {
        'os': platform.platform(),
        'python_version': platform.python_version(),
        'hostname': platform.node(),
        'db_password': DB_PASSWORD,
        'api_key': API_KEY
    }
    return info