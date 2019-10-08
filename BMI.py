# -*- coding: UTF-8 -*-

weight = eval(input("請輸入體重(公斤): "))

height = eval(input("請輸入身高(公分): "))

#計算BMI
weightInKilograms = weight
heightInMeters = height / 100
bmi = weightInKilograms / ( heightInMeters ** 2 )

print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("體重不足")
elif bmi < 24:
    print("正常")
elif bmi < 30:
    print("輕度肥胖")
elif bmi < 35:
    print("輕度肥胖")
else:
    print("重度肥胖")