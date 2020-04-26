#!/bin/python 
import os
import math
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Laboratorio de alturas de piramides según eñ número de cubos

blocks = int(input("Enter the number of blocks: "))

# Tengo la siguiente situación:
# Para tener: 
#  1) altura          2) alturas          3) alturas            4) alturas          5) alturas
# Necesito que:
#                       *                       *                    *                      *       | 1
#  *                   * *                     * *                  * *                    * *      | 2
#                                             * * *                * * *                  * * *     | 3
#                                                                 * * * *                * * * *    | 4
#                                                                                       * * * * *   | 5
# Los saltos son proporcionales porque son sumando 1 unidad.
#           +2                  +3                      +4                      +5
# Para saber qué número de bloques necesita cada altura es aplicando:
#
#  bloques = (h * (h + 1)) / 2
#
# Como el problema a resolver es el contrario, aplico la inversa de la operación:
#
# bloques * 2 = h ( h + 1) ==> Altura (H)
# H => ((2*bloques) -h^2-h) = 0
# H => h^2+h-(2*bloques)=0
#
# Descartamos los valores negativos de la operación cuadrática y tenemos la altura.

# Inicializamos con la altura mínima que es 1 
h=1
# Resolvemos la ecuación de segundo grado:
# (h^2 + h - (2*blocks))                            =======> (-b +- sqrt ("b^2)-4*a*c))/2*a
# Los valores son:
# a: 1
# b: 1
# c: nº de bloques de entrada

a = h
b = h
c = -blocks*2
print("--------------")
print(a)
print(c)
print("--------------")
interior = ((b**2)-(4*a*c))
eq1 = (-b + math.sqrt(interior))/2
# El resultado de eq2 se deshecha porque no son válidos valores negativos
eq2 = (-b - math.sqrt(interior))/2

print("The height of the pyramid: ",  eq1)
print("The eq2 value is: ",  eq2)
while eq1 >= 0:
    print("Vuelta nº:" + blocks )
    blocks -= 1
    eq1 -= 1
