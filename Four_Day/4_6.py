'''
Author: your name
Date: 2020-12-13 11:43:08
LastEditTime: 2020-12-13 11:43:09
LastEditors: Please set LastEditors
Description: 带有外部状态的生成器函数
FilePath: \python\Four_Day\4_6.py
'''
from collections import deque


class linehistory(object):
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=history)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


