#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: The Beatles List.

# Paso 1. Crear lista
beatles = []

# Paso 2. Uso de append() - añadir a la lista
beatles.append("Jonh Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Paso 3. Bucle FOR y append() para pedir al usuario que agregue a 
# Stu Sutcliffe 
# Pete Best.
l = len(beatles)
for i in range(l+1):
    addList = input("Please, Add Stu and Pete in the Beatle List: ") 
    beatles.append(addList)

# Paso 4. Eliminar a Stu y Pete de la lista
print("Step 4")
print(beatles)
delList = input("Who delete of list? (Position) ")
del beatles[delList]