#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: What is the output of the following snippet?

lst = [1, 2, 3, 4, 5]
lst2 = []
add = 0

for number in lst:
    add += number
    lst2.append(add)

print(lst2) # 1,3,6,10,15