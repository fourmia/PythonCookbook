'''
Author: your name
Date: 2020-12-19 17:06:56
LastEditTime: 2020-12-19 17:12:18
LastEditors: Please set LastEditors
Description: 定义有默认参数的函数
FilePath: \python\Seven_Day\7_5.py
'''

_no_value = object()


def spam(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    else:
        print(b)


def main():
    spam(1)
    spam(1, 2)
    spam(1, None)


if __name__ == '__main__':
    main()
