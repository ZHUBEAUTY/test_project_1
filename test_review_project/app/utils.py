# 无用导入
import json
import sys
import os

# 函数无注释、无参数校验
def format_data(d):
    r = []
    for k, v in d.items():
        r.append(v)
    return r

# 全局变量滥用
count = 0
def add_count():
    global count
    count += 1
    