'''
Author: your name
Date: 2020-12-05 21:16:06
LastEditTime: 2020-12-05 21:50:04
LastEditors: Please set LastEditors
Description: 字符串匹配, match总是从最开始进行匹配， findall查找任意位置
FilePath: \python\Two_Day\2_4.py
'''
import re


def match_str_with_re(text, regex):
    datepat = re.compile(regex)
    print(datepat.findall(text))
    # print(dir(datepat.match(text)))


def main():
    text = 'Today is 11/27/2012, PyCon starts 3/13/2013'
    regex = r'(\d+)/(\d+)/(\d+)'
    match_str_with_re(text, regex)

if __name__ == '__main__':
    main()

