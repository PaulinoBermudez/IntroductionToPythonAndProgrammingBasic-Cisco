#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Hipótenisis de Collatz
#   Dice que un nº natural positivo distinto de cero, sí es:
#      1 - Un nº par 
#           + lo divido entre 2
#      2 - Un nº impar 
#           + lo multiplico x 3
#           + y le sumo +1
#      3 - Y vuelvo a hacer lo mismo (Pasos 1 ó 2)
# El misterio está en que todos los nºs llegan a 1.

c0 = int(input("Write a number possitive: "))
for i in range (c0):
    print("........................................................................................................ ", i)
    if c0 <= 0:
        print(".............................................. 0")
        print("Error in your input, data is not valied")
    else:
        while i < c0:
            if c0 % 2 == 0:
                print(".............................................. x2")
                c0 = c0/2
                i += 1
                print(i , " - " , int(c0))
            else:
                print(".............................................. x3")
                c0 = (3 * c0 + 1)
                i += 1
                print(i , " - " , int(c0))
        
