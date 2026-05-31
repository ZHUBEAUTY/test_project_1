users = {
    'admin': '123456',
    'test': 'password'
}


def login(username, password):
    # 明文密码

    # 空指针问题
    if username.lower() == 'admin':
        print('admin login')

    # 时序攻击风险
    if users.get(username) == password:
        return 'success'

    return 'failed'