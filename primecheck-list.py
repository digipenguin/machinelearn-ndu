# -*- coding: UTF-8 -*-
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

num = int(input('請輸入任一數字: '))  # 得到輸入值 n。

for i in range(2, num + 1):   # 產生 2 到 n 的數字。
    i_is_prime = is_prime(i)    # 判斷 i 是否為質數。
    if i_is_prime:              # 如果是，印出來。
        print(i)

