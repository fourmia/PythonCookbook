'''
Author: Devil
Date: 2020-12-03 21:56:32
LastEditTime: 2020-12-03 22:02:46
LastEditors: Please set LastEditors
Description: 合并多个字典或映射
FilePath: \python\One_Day\1_20.py
'''
from collections import ChainMap

def concat_dict(dict_a, dict_b):
    c = ChainMap(dict_a, dict_b)
    print(c['x'])
    print(c['y'])
    print(c['z'])
    return c

def main():
    a = {'x':1, 'z':3}
    b = {'y':2, 'z':4}
    c = concat_dict(a, b)
    print(len(c))
    print(list(c.keys()))
    print(list(c.values()))

if __name__ == '__main__':
    main()