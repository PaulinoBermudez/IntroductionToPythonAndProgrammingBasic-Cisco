#!/bin/python
import os
os.system("clear")
os.system("cls")

intro = input ("""

    Usando las mismas variables del ejercicio anterior, qué obtenemos:

    - x > z
    - (y - 5) == x

    Pulse ENTER para continuar.
""")


x,y,z = 5,10,8

# 5 > 8 => False
print(x > z)
# (10 - 5) == 5 => True
print((y-5) == x)