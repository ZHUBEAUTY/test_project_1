
# 硬编码数据库密码（严重安全漏洞）
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "blog_admin",
    "password": "blog@123456",
    "database": "mini_blog"
}

import sqlite3
# 全局连接（并发问题）
conn = sqlite3.connect(**DB_CONFIG)
cursor = conn.cursor()

# SQL注入核心方法（被auth.py/blog.py调用）
def db_query(sql):
    # 无异常处理、直接执行SQL
    cursor.execute(sql)
    return cursor.fetchall()

def db_execute(sql):
    cursor.execute(sql)
    conn.commit()
    # 数据库连接永不关闭（资源泄漏）