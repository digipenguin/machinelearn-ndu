# -*- coding: UTF-8 -*-
import datetime

inputDate = input("Enter the date in format 'mm/dd/yyyy' : ")

month,day,year = inputDate.split('/')

isValidDate = True
try :
    datetime.datetime(int(year),int(month),int(day))
except ValueError :
    isValidDate = False

if(isValidDate) :
    print ("輸入的日期正確")
else :
    print ("輸入的日期錯誤")