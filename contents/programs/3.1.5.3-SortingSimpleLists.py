#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Sorting simple lists - The bubble sort algorithm.

mylist = []
swapped = True 
num = int(input("How many elements do you want to sort: "))
for i in range(num):
    val = float(input("Enter a list element: "))
    mylist.append(val)
while swapped:
    swapped = False
    for i in range (len(mylist) - 1):
        if mylist[i] > mylist[i + 1]:
            swapped = True
            mylist[i], mylist[i+1] = mylist[i+1], mylist[i]
print("\n Sorted: ")
print(mylist)