'''
Author: Devil
Date: 2020-12-03 21:47:37
LastEditTime: 2020-12-03 21:55:13
LastEditors: Please set LastEditors
Description: 转换同时并计算数据
FilePath: \python\One_Day\1_19.py
'''
def clc_and_change(nums):
    s = sum(x * x for x in nums)
    return s


def main():
    nums = [1, 2, 3, 4, 5]
    data_sum = clc_and_change(nums)
    print(data_sum)

if __name__ == '__main__':
    main()