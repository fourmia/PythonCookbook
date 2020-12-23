'''
Author: your name
Date: 2020-12-16 21:37:52
LastEditTime: 2020-12-16 21:58:36
LastEditors: Please set LastEditors
Description: 顺序迭代合并后的排序迭代对象
FilePath: \python\Four_Day\4_15.py
'''
import heapq

def main():
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]
    for c in heapq.merge(a, b):
        print(c)

if __name__ == "__main__":
    main()