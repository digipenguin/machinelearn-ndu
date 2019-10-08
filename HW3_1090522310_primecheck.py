# -*- coding: UTF-8 -*-

num = int(input("請輸入任一數字: "))


if num > 1:

    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是質數")
            break
    else:
        print(num, "是質數")

else:
    print(num, "不是質數")
