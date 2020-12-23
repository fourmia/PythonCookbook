'''
Author: your name
Date: 2020-12-06 11:37:07
LastEditTime: 2020-12-06 12:01:40
LastEditors: Please set LastEditors
Description: 字符串中插入变量 format, format_map vars
FilePath: \python\Two_Day\2_9.py
'''
import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

class safesub(dict):
    """防止key找不到"""
    def __missing__(self, key):
        return '{' + key + '}'

def main():
    name = 'Guido'
    n = 37
    print(sub('Hello {name}'))
    print(sub('Your favorite color is {color}'))

if __name__ == '__main__':
    main()

