# 映射名称到序列元素
import numpy as np
import pandas as pd
from collections import namedtuple

def main():
    Subscribe = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscribe('jonesy@example.com', '2020-12-01')
    print(sub)
    print(sub.addr)
    print(sub.joined)

if __name__ == "__main__":
    main()