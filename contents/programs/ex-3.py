#!/bin/python
import os
os.system("clear")
os.system("cls")

intro = input("""

    What's the output of the following snippet?

    +- x,y,z = 5,10,8 
    |  x,y,z = z,y,x
    |  print(x > z)
    |> print((y - 5)  == x)

    ENTER to continue...
""")

print("Define the variables")
x,y,z = 5,10,8 
print("Re-defined the new values of variables")
print("""
    x = z => x = 8 
    y = y => y = 10 
    z = x => z = 5
""")
x,y,z = z,y,x
print ("Check the result")
print(x,y,z)
print()
print(x > z) # True
print((y - 5)  == x) # False