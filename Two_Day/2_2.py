'''
Author: Devil
Date: 2020-12-03 22:15:23
LastEditTime: 2020-12-03 22:26:52
LastEditors: Please set LastEditors
Description: 字符串开头或结尾匹配
FilePath: \python\Two_Day\2.2.py
'''
import os

def choose_ftype(filetuple):
    res =  [name for name in filetuple if name.endswith(('.c', '.h'))]
    print(res)
    print(any(name.endswith('.py') for name in filetuple))

def main():
    filetuple = tuple(['Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h'])
    choose_ftype(filetuple)

if __name__ == "__main__":
    main()