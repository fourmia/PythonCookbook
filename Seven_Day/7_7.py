'''
Author: your name
Date: 2020-12-19 17:32:58
LastEditTime: 2020-12-19 17:57:57
LastEditors: Please set LastEditors
Description: 在匿名表达式中设置默认参数
FilePath: \python\Seven_Day\7_7.py
'''


def lambda_test():
    funcs = [lambda x: x + n for n in range(5)]
    for f in funcs:
        print(f(0))
    print('*' * 20)
    funcs = [lambda x, n=n: x + n for n in range(5)]
    for f in funcs:
        print(f(0))


def main():
    lambda_test()


if __name__ == '__main__':
    main()