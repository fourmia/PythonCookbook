'''
Author: your name
Date: 2020-12-19 16:40:38
LastEditTime: 2020-12-19 16:52:24
LastEditors: Please set LastEditors
Description: 可接受任意数量参量的函数
FilePath: \python\Seven_Day\7_1.py
'''

import html


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    print(keyvals)
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value)
    )
    return element

def main():
    print(make_element('item', 'Albatross', size='large', quantity=6))
    print(make_element('p', '<spam>'))

if __name__ == '__main__':
    main()

