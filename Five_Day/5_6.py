'''
Author: your name
Date: 2020-12-19 11:30:33
LastEditTime: 2020-12-19 11:38:38
LastEditors: Please set LastEditors
Description: 使用创建类文件对象的程序来创建I/O
FilePath: \python\Five_Day\5_1.py
'''
import io

def string_io():
    s = io.StringIO()
    s.write('Hello World\n')
    print('This is a test!', file=s)
    print(s.getvalue())

    s = io.StringIO('Hello\nWorld\n')
    print(s.read(4))
    print(s.read())
    s.seek(0)
    print(s.read())

def main():
    string_io()

if __name__ == "__main__":
    main()

