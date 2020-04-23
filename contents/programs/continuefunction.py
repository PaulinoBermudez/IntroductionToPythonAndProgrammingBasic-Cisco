#!/bin/python 
import os
from datetime import date
os.system('clear')
os.system('cls')

# @author: [ Paulino Bermúdez R.]
# @Description: Continue function. 
print(40*'·')
print(date.today())
print(40*'·')

largestNumber = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1
    if number > largestNumber:
        largestNumber = number
    number = int(input("Enter a number or type -1 to end program: "))

if counter:
    print("The largest number is", largestNumber)
else:
    print("You haven't entered any number.")

