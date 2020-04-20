#!/bin/python

import os
os.system("clear")
os.system("cls")

while True:
    x=input("Enter a number to count to: ")
    if x == 'q' or x == 'quit':
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y+=1
        if y>x:
            break 
        