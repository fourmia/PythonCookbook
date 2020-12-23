'''
Author: Devil
Date: 2020-12-03 22:06:06
LastEditTime: 2020-12-03 22:12:52
LastEditors: Please set LastEditors
Description: 使用界定符分割字串
FilePath: \python\Two_Day\2_1.py
'''
import re

def split_from_re(lines, regex):
    res = re.split(regex, lines)
    return(res)

def main():
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    regex = r'(?:,|;|\s)\s*'
    res = split_from_re(line, regex)
    print(res)

if __name__ == '__main__':
    main()