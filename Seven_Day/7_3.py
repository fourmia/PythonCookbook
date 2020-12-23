'''
Author: your name
Date: 2020-12-19 16:59:54
LastEditTime: 2020-12-19 17:04:00
LastEditors: Please set LastEditors
Description: 函数参数增加元信息(类型注解)
FilePath: \python\Seven_Day\7_3.py
'''
import typing


def add(x: int, y: int) -> int:
    return x+y


def main():
    print(help(add))
    print(add.__annotations__)


if __name__ == '__main__':
    main()
