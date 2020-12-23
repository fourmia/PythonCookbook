'''
Author: your name
Date: 2020-12-06 11:12:12
LastEditTime: 2020-12-06 11:28:51
LastEditors: Please set LastEditors
Description: 删除字符串中不需要的字符 strip处理开始结尾空格， repalce
FilePath: \python\Two_Day\2_8.py
'''
def del_space(text):
    s = text.strip()
    print(s)
    print(s.replace(' ', ''))

def main():
    text = 'hello  world \n'
    del_space(text)

if __name__ == '__main__':
    main()