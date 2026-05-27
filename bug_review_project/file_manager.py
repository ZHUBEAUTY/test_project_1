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

    return config