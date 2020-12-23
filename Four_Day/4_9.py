'''
Author: your name
Date: 2020-12-16 20:56:27
LastEditTime: 2020-12-16 21:22:13
LastEditors: Please set LastEditors
Description: 排列组合迭代
FilePath: \python\Four_Day\4_9.py
'''
from itertools import permutations, combinations

def test_permu(items):
    for p in permutations(items):
        print(p)
    
    for p in permutations(items, 2):
        print(p)

def test_combin(items):
    for p in combinations(items, 2):
        print(p)


def main():
    items = ['a', 'b', 'c']
    test_permu(items)
    test_combin(items)

if __name__ == '__main__':
    main()