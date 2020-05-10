#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: 

i = 0
while i <= 3:
    i += 2
    print("*----------")

i = 0
while i <= 5: 
    i += 1
    if i % 2 == 0: 
        break 
    print("+")

for y in range(1):
    print("@")
else:
    print("@")

var = 0
while var < 6:
    var +=1
    if var %2 == 0:
        continue
    print("#")

v = 1 
while v < 10:
    print("---------&")
    v = v << 1
    print(v)

z = 10 
y = 0

X = y < z and z > y or y > z and z < y
print(X)



lst = [ 3, 1, -2]
print(lst[lst[-1]])

lst = [1,2,3,4]
print(lst[-3:-2])

from random import random

for i in range(5):
    r = (random()*100)
    print("Sus probabilidades son: {:e}".format(r))

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
print(python_implementation)