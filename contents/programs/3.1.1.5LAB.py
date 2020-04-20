#!/bin/python
import os
os.system("clear")
os.system("cls")

print('''
    This program print the block in function of input number.
    And, you exit write '-1' on screen.
''')

while True:
    parameter=int(input("Write the parameter: "))
    if parameter == -1:
        break
    elif parameter < 100:
        print("False \n __________________________")
    else:
        print("True \n __________________________")