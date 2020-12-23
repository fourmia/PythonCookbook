'''
Author: your name
Date: 2020-12-19 17:13:53
LastEditTime: 2020-12-19 17:28:20
LastEditors: Please set LastEditors
Description: 定义匿名、内联函数
FilePath: \python\Seven_Day\7_6.py
'''


def sorted_name():
    names = [
        "David Beazley", 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder'
    ]
    print(sorted(names, key=lambda name: name.split()[-1].lower()))


def main():
    sorted_name()


if __name__ == '__main__':
    main()