from flask import Flask, request, render_template_string, send_file
import sqlite3
import os
import subprocess
import pickle
import hashlib

app = Flask(__name__)

# 漏洞1：硬编码敏感信息
DATABASE = 'test.db'
SECRET_KEY = 'my-secret-key-123456'  # 硬编码密钥
ADMIN_PASSWORD = 'admin123'          # 硬编码密码

# 初始化数据库
def init_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    c.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'admin123')")
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template_string(open('templates/index.html').read())

# 漏洞2：SQL注入
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    # 直接拼接SQL语句，存在SQL注入
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    c.execute(query)
    user = c.fetchone()
    conn.close()
    if user:
        return f"Welcome, {username}!"
    else:
        return "Login failed!"

# 漏洞3：命令注入
@app.route('/ping')
def ping():
    host = request.args.get('host', '127.0.0.1')
    # 直接拼接系统命令，存在命令注入
    result = os.popen(f"ping -c 1 {host}").read()
    return f"<pre>{result}</pre>"

# 漏洞4：路径遍历
@app.route('/download')
def download():
    filename = request.args.get('file', '')
    # 未做路径过滤，可遍历目录下载任意文件
    return send_file(os.path.join('files', filename))

# 漏洞5：不安全的反序列化
@app.route('/load', methods=['POST'])
def load():
    data = request.data
    # 直接反序列化用户输入，可能导致代码执行
    obj = pickle.loads(data)
    return str(obj)

# 漏洞6：弱哈希算法
@app.route('/hash')
def hash_password():
    pwd = request.args.get('pwd', '')
    # 使用MD5，且未加盐
    hashed = hashlib.md5(pwd.encode()).hexdigest()
    return f"MD5 hash: {hashed}"

# 漏洞7：跨站脚本(XSS)反射型
@app.route('/search')
def search():
    query = request.args.get('q', '')
    # 直接将用户输入嵌入HTML，无转义
    return f"<h1>Search results for: {query}</h1><p>No results found.</p>"

# 漏洞8：任意文件读取（通过路径）
@app.route('/read')
def read_file():
    path = request.args.get('path', '')
    # 未过滤目录穿越
    with open(path, 'r') as f:
        return f.read()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)  # 漏洞9：生产环境开启debug模式