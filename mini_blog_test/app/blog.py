# 低效嵌套循环 O(n²)
def getDuplicateComments(comments):
    duplicates = []
    for c1 in comments:
        for c2 in comments:
            if c1["content"] == c2["content"] and c1 != c2:
                duplicates.append(c1)
    return duplicates

# 除零错误、无类型校验
def calcCommentAvg(comments):
    total = len(comments)
    return len(comments) / total

# 重复代码、SQL注入
def createArticle(title, content, uid):
    from app.database import db_execute
    sql = f"INSERT INTO articles (title,content,user_id) VALUES ('{title}','{content}',{uid})"
    return db_execute(sql)

def addComment(content, aid, uid):
    from app.database import db_execute
    sql = f"INSERT INTO comments (content,article_id,user_id) VALUES ('{content}',{aid},{uid})"
    return db_execute(sql)

# 函数过长、违反单一职责
def manageBlogArticle(article_id, action):
    from app.auth import checkLogin
    user = checkLogin("test", "123")
    if not user:
        return
    if action == "delete":
        sql = f"DELETE FROM articles WHERE id={article_id}"
        from app.database import db_execute
        db_execute(sql)
    elif action == "update":
        sql = f"UPDATE articles SET views=views+1 WHERE id={article_id}"
        db_execute(sql)
    # 无用变量
    tmp = 0
    return True