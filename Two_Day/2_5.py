'''
Author: your name
Date: 2020-12-05 21:50:58
LastEditTime: 2020-12-05 22:07:14
LastEditors: Please set LastEditors
Description: 字符串搜索及替换，str.repalce(), re.sub(), 替换回调函数
FilePath: \python\Two_Day\2_5.py
'''
import re

def replace_strings(text, regex, sub):
    datepat = re.compile(regex)
    res = datepat.sub(sub, text)
    print(res)

def main():
    text = 'Today is 11/27/2012, PyCon starts 3/13/2013'
    regex = r'(\d+)/(\d+)/(\d+)'
    sub = r'\3-\1-\2'
    replace_strings(text, regex, sub)

if __name__ == '__main__':
    main()