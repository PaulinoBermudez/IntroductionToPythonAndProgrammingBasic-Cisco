#!/bin/python
import os
os.system("clear")
os.system("cls")

intro = input("""

What's the output of the following snippet?

 +---x = 10 
 |   if x == 10:
 |       print( x == 10)
 |   if x > 5:
 |       print(x > 5)
 |   if x < 10:
 |       print(x < 10)
 |   else:
 |       print("else:")
 +--- END


ENTER to continue...
""")


x = 10 
if x == 10:
    print( x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else:")