'''
Author: your name
Date: 2020-12-16 21:25:05
LastEditTime: 2020-12-16 21:30:03
LastEditors: Please set LastEditors
Description: 不同元素集合上的迭代
FilePath: \python\Four_Day\4_12.py
'''
from itertools import chain



def test_chain():
    a = [[1,2,3,4],['x','y','z']]
    res =[x for x in chain(*a)]
    print(res)
    print(len(res))

def main():
    test_chain()


if __name__ == "__main__":
    main()