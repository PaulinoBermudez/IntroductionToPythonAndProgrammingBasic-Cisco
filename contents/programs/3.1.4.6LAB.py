#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Introduction of list. INTRO (Se puede mejorar y MUCHO)

while True:
    hatList = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
    mido = len(hatList)
    print("_______________________ INICIO \n Longitud actual", mido, "\n Lista actual" , hatList, "\n_______________________\n\n")
    # Step 1: write a line of code that prompts the user to replace the middle number with an integer number entered by the user.
    print("_______________________ PASO 1. - PEDIR UN NUMERO Y REMPLAZARLO EN LA LISTA. \n") 
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    num = int(input("Write a numeber:"))
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n")
    mitad = int(mido/2) 
    print("_______________________ CALCULO DE LA MITAD DE LA LISTA \n La mitad de la lista es: ",mitad , " \n_______________________ \n\n")
    hatList[mitad] = num
    print("Lista nueva", hatList)
    # Step 2: write a line of code here that removes the last element from the list.
    print("_______________________ PASO 2. - ELIMINA ÚLTIMA ENTRADA.")
    nuevaMedida = len(hatList)
    print(nuevaMedida)
    print()
    del hatList[nuevaMedida-1]
    print("Ahora la lista es: ", hatList)
    # Step 3: write a line of code here that prints the length of the existing list.
    print("_______________________ PASO 3. - NUEVA LONGITUD DE LA LISTA.")
    midoTres = len(hatList)
    print("_______________________ ")
    print("Longitud del paso 3 es: ", midoTres , "\n Última lista: ",hatList, " \n_______________________ \n\n")
    fin = input("Pulse Q para finalizar: ")
    if fin == 'Q'or fin == 'q': 
        break
