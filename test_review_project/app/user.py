# 无文档字符串、命名不规范
def getUserInfo(uId):
    # 未处理空值
    if uId < 0:
        return
    # 调用db模块存在SQL注入
    from app.db import query
    sql = f"SELECT * FROM users WHERE id = {uId}"
    user = query(sql)
    
    # 变量未使用
    tmp = 12345
    # 循环边界错误
    for i in range(5):
        print("加载用户数据")
    
    # 文件未关闭
    f = open("user_log.txt", "a")
    f.write(f"user {uId} accessed\n")
    return user

# 函数过长、违反单一职责
def process_all_users(users):
    valid = []
    for u in users:
        if u and u.get("id"):
            valid.append(u)
    
    total = 0
    for u in valid:
        total += u.get("age", 0)
    
    f = open("stats.txt", "w")
    f.write(str(total))
    return valid, total
