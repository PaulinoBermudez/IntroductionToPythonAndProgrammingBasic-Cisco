
#!/bin/python
import os
os.system("clear")
os.system("cls")

intro = input("""

What is the output of the following snippet?
            
        x = 1   -> Integer
        y = 1.0 -> Float value
        z = "1"  -> Yes! it's a string

        if x == y:
            one
        if y == int(z):
            two
        elif x == y:
            three
        else:
            four


ENTER to continue...
""")

x = 1 
y = 1.0
z = "1"  

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")