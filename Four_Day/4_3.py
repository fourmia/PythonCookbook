'''
Author: your name
Date: 2020-12-13 10:27:55
LastEditTime: 2020-12-13 10:31:09
LastEditors: Please set LastEditors
Description: 使用生成器创建新的迭代模式
FilePath: \python\Four_Day\4_3.py
'''

def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


def main():
    for n in frange(0, 4, 0.5):
        print(n)

if __name__ == '__main__':
    main()
