'''
Author: your name
Date: 2020-12-16 20:45:05
LastEditTime: 2020-12-16 20:53:07
LastEditors: Please set LastEditors
Description: 迭代器切片
FilePath: \python\Four_Day\4_7.py
'''
import itertools

def count(n):
    while True:
        yield n
        n += 1

def main():
    c = count(0)
    print(next(c))
    print(next(c))
    print(list(itertools.islice(c, 10, 20)))
    #c[10:20]

if __name__ == "__main__":
    main()