#!\bin\python

import os
clear=os.system("clear")
clear=os.system("cls")
clear
# El único detalle que hay que realizar es cambiar la 'w' de write por una 'a' de add 
# en el modo de ejecución del fichero.
file=open("devices.txt","a")

while True:
    newItem=input("Enter devices name: ")
    if newItem == "exit":
        print("All done!")
        print("")
        file=open("devices.txt","r")
        for item in file:
            print(item.strip())
        file.close()
        break
    file.write(newItem + "\n")
    print("Added devices!")
    clear
