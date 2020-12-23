'''
Author: your name
Date: 2020-12-13 11:15:28
LastEditTime: 2020-12-13 11:42:31
LastEditors: Please set LastEditors
Description: 反向迭代序列, reversed; 自定义序列 __reversed__()
FilePath: \python\Four_Day\4_5.py
'''

class Countdown():
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            print(n*'-')
            n -= 1
    
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1
    
def main():
    """
    for rr in reversed(Countdown(30)):
        print(rr)
    """
    for rr in Countdown(30):
        print(rr)

if __name__ == '__main__':
    main()


