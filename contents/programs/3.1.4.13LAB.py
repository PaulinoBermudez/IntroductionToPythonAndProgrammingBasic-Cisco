#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: The Beatles List.

# Paso 1. Crear lista
print("························Step. 1 \n")
beatles = []
print(beatles,"\n")
# Paso 2. Uso de append() - añadir a la lista
print("························Step. 2 \n")
beatles.append("Jonh Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Beatles List ", beatles ,"\n")
# Paso 3. Bucle FOR y append() para pedir al usuario que agregue a 
# Stu Sutcliffe 
# Pete Best.
print("························Step. 3 \n")
l = len(beatles)
for i in range(l+2):
    addList = input("Please, Add Stu and Pete in the Beatle List: ") 
    beatles.append(addList)
    print("\n", beatles,"\n")
# Paso 4. Eliminar a Stu y Pete de la lista
print("························Step 4 \n")
print(beatles)
delList = int(input("Who delete of list? (Position) "))
del beatles[delList]
# Añadir con insert() a Ringo Starr al comienzo de la lista
print("························Step 5. \n")
beatles.insert(0, "Ringo Starr")