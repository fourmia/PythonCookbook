'''
Author: your name
Date: 2020-12-05 21:01:00
LastEditTime: 2020-12-05 21:15:25
LastEditors: Please set LastEditors
Description: 采用shell通配符来匹配字符串
FilePath: \python\Two_Day\2_3.py
'''
from fnmatch import fnmatch, fnmatchcase


def get_string_form_shell(names, shell_str):
    res = [name for name in names if fnmatch(name, shell_str)]
    print(res)


def main():
    names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
    shell_str = r'Dat[0-9].csv'
    get_string_form_shell(names, shell_str)

if __name__ == '__main__':
    main()
