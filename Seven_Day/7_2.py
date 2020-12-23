'''
Author: your name
Date: 2020-12-19 16:53:36
LastEditTime: 2020-12-19 16:59:28
LastEditors: Please set LastEditors
Description: 只接受关键字参数的函数
FilePath: \python\Seven_Day\7_2.py
'''


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


def main():
    print(mininum(1, 5, 2, -5, 10))
    print(mininum(1, 5, 2, -5, 10, clip=0))


if __name__ == '__main__':
    main()
