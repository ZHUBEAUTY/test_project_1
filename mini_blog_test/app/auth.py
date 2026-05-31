# 命名不规范、无文档字符串
def checkLogin(u, p):
    # SQL注入高危漏洞
    from app.database import db_query
    sql = f"SELECT * FROM users WHERE username='{u}' AND password='{p}'"
    user = db_query(sql)
    
    # 未处理空值：用户不存在会直接报错
    return user[0]

# 路径遍历漏洞（读取任意文件）
def getUserAvatar(filename):
    # 未校验路径，可读取 /etc/passwd
    with open(f"avatars/{filename}", "r") as f:
        return f.read()

# 全局变量滥用、无异常处理
login_count = 0
def recordLogin():
    global login_count
    login_count += 1
    # 文件未关闭
    log = open("logs/auth.log", "a")
    log.write(f"login {login_count}\n")