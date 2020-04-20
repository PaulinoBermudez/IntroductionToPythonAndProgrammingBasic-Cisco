#!/bin/python
import os
os.system("clear")
os.system("cls")

while True:
    year = int(input("Enter a year: "))
    print("Data: ", year)
    if year == 0:
        print("Exit program")
        break
    elif year == 1580:
        print("Not within the Gregorian calendar period")
    elif year % 4 == 0:
        # print("{:} resto 0 al dividir por 4.".format(year))
        if year % 100 != 0:  
            print("{:} is a leap year".format(year))
            # print("{:} resto 0 al dividir por 100.".format(year))
        if year % 400 == 0:
            # print("{:} resto 0 al dividir por 400.".format(year))
            print("{:} is a leap year".format(year))
    elif year % 4 != 0:
        print("{:} Common year".format(year))
    else:
        print("Input fail")