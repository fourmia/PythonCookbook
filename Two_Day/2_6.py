'''
Author: your name
Date: 2020-12-05 22:13:26
LastEditTime: 2020-12-06 10:56:06
LastEditors: Please set LastEditors
Description: 忽略大小写搜索替换字符串
FilePath: \python\Two_Day\2_6.py
'''
import re

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace


def main():
    text = r'UPPER PYTHON, lower python, Mixed Python'
    res = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
    print(res)

if __name__ == '__main__':
    main()