'''
Author: your name
Date: 2020-12-06 10:58:36
LastEditTime: 2020-12-06 11:07:16
LastEditors: Please set LastEditors
Description: 多行匹配,采用非捕获组添加对换行的支持
FilePath: \python\Two_Day\2_7.py
'''
import re

def match_mulitline_with_re(text, regex):
    comment = re.compile(regex)
    print(comment.findall(text))

def main():
    text = r'''/* this is a 
    multiline comment */'''
    regex = r'/\*((?:.|\n)*?)\*/'
    match_mulitline_with_re(text, regex)

if __name__ == '__main__':
    main()