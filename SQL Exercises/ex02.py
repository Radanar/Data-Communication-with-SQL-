# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 15:52:06 2023

@author: HP
"""

x = 2
y = 14

result = x * x * x * x
print("My result is: ", result)
result2 = pow(x,y)
print("My result2 is: ", result2)

print("--------------------")
mylist = [3,5,6,8,2,7,8]
print(mylist)

print(len(mylist))

print("--------------------")
for x in range(10):
    print("The value of x = ", x)

print("--------------------")
for y in mylist:
    print(y)
    
mygrade = 90

if mygrade >= 90:
    print("Excellent")
elif mygrade >=80:
    print("very good")
elif mygrade >=70:
    print("good")    
else:
    print("Fail")
    
print("Hello")