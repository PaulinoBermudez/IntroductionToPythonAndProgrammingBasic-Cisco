#!/bin/python
import os
os.system("clear")
os.system("cls")

intro = input("""
    El ejercicio consiste en comparar 3 variables con valores:
    x = 5
    y = 10
    z = 8
    Indicar cual es la salida por pantalla que tendrán las comparaciones siguientes:
    
    - (x > y)
    - (y > z)

    Pulse ENTER para continuar
""")


x = 5 
y = 10 
z = 8 

print(x > y)
print(y > z)
