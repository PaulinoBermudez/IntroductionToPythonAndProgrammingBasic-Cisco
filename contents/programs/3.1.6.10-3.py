#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Ejercicio 3 de la seccion 3.1.3.10
l1 = ["A", "B", "C"]
l2 = l1
l3 = l2

del l1[0]
del l2[:]

print(l3)