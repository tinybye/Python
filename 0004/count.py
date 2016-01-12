# -*- coding: utf-8 -*-

import re

def count(filepath):
    #读取文件
    f = open(filepath, 'r')
    s = f.read()
    #正则表达式进行字符串匹配查找单
    words = re.findall(r'[a-zA-Z0-9]+', s)
    return len(words)

print(count('word.txt'))
