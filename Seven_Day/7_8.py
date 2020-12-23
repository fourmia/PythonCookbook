'''
Author: your name
Date: 2020-12-19 17:58:37
LastEditTime: 2020-12-19 18:09:46
LastEditors: Please set LastEditors
Description: 减少可调用参数个数
FilePath: \python\Seven_Day\7_8.py
'''
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
import math
from functools import partial


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


def main():
    pt = (4, 3)
    points.sort(key=partial(distance, pt))
    print(points)


if __name__ == '__main__':
    main()
