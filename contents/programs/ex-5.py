
#!/bin/python
import os
os.system("clear")
os.system("cls")

intro = input("""

What is the output of the following snippet?
            
    x = "1" -> STRING!

    if x == 1:
        one
    elif x == "1":
        if int(x) > 1:
            two
        elif int(x) < 1:
            three
        else:
            four
    if int(x) == 1:
        five
    else:
        six


ENTER to continue...
""")

x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
       print(" four")
if int(x) == 1:
    print("five")
else:
    print("six")
