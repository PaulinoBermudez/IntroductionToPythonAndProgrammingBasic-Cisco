#!/bin/python
import os
os.system("clear")
os.system("cls")

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

print(type(secret_number))

number= int(input("Write a number and good luck! :"))

while number != secret_number:
    print("\n Ha ha! You're stuck in my loop! ... Try again")
    number= int(input(" Write a number and good luck! -> "))

print()    
print(32*"*" + "\n Well done, muggle! You are free now. \n" + 32*"*")
