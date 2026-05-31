import sqlite3


def get_user(username):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()

    # SQL注入
    query = f"SELECT * FROM users WHERE username = '{username}'"

    cursor.execute(query)

    result = cursor.fetchall()

    conn.close()

    return result



def insert_user(username, age):
    conn = sqlite3.connect('test.db')

    # 未使用事务
    conn.execute(
        f"INSERT INTO users VALUES('{username}', {age})"
    )

    # 未commit
    conn.close()



def batch_insert(users):
    conn = sqlite3.connect('test.db')

    for user in users:
        conn.execute(
            f"INSERT INTO users VALUES('{user['name']}', {user['age']})"
        )

    # 性能问题
    conn.commit()
    conn.close()