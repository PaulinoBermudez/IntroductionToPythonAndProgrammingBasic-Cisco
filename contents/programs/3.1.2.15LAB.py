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
loop = 0
for i in range (c0+1):
    #print("........................................................................................................ ", i)
    if c0 <= 0:
        print(".............................................. Error")
        print("Error in your input, data is not valied")
    else:
        #print("..............................................")
        #print("                                              ", i)
        #print("..............................................")
        while c0 >= i:
            if c0 % 2 == 0:
                print("...............................................", loop, "Nº - Par")
                c0 = c0/2
                i += 1
                loop +=1
                print(" ===> " , int(c0))
            else:
                print("...............................................", loop, "Nº - Impar")
                c0 = (3 * c0 + 1)
                i += 1
                loop +=1
                print(" ===> " , int(c0))
    
print("Loops: ", i+1)        
print("Steps: ", loop+1)
