# 硬编码密码（严重安全问题）
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "123456"
DB_NAME = "test"

import pymysql
def query(sql):
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    cursor = conn.cursor()
    # 直接执行用户传入SQL → SQL注入
    cursor.execute(sql)
    return cursor.fetchall()

def execute(sql):
    conn = pymysql.connect(DB_HOST, DB_USER, DB_PASS, DB_NAME)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    # 无异常处理、连接不关闭