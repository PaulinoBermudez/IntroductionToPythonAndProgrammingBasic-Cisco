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
for i in range(2):
    l = len(beatles)
    addList = input("Please, Add Stu and Pete in the Beatle List: ") 
    beatles.append(addList)
    print("\n", beatles,"\n")
    print("The length is: ", l+1)
# Paso 4. Eliminar a Stu y Pete de la lista
print("························Step 4 \n")
borra = int(input("How many user delete? "))
for i in range(borra):
    l = int(len(beatles))
    print(beatles)
    delList = int(input("Who delete of list? (Position [0-{:2}]) ".format(l-1)))
    del beatles[delList]
    print("OKEY! - Update... \n")
# Añadir con insert() a Ringo Starr al comienzo de la lista
print("\n ························Step 5. \n Adding Ringo a Beatle group.")
beatles.insert(0, "Ringo Starr")
print("The final list is: ", beatles)