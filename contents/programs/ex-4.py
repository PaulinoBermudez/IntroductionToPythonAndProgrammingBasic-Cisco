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