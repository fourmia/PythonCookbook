'''
Author: your name
Date: 2020-12-06 21:45:29
LastEditTime: 2020-12-06 21:49:08
LastEditors: Please set LastEditors
Description: 手动遍历迭代器
FilePath: \python\Four_Day\4_1.py
'''

def use_next(items):
    print(next(items))
    print(next(items))
    print(next(items))
    print(next(items))

def main():
    items = iter([1,2,3])
    use_next(items)

if __name__ == '__main__':
    main()