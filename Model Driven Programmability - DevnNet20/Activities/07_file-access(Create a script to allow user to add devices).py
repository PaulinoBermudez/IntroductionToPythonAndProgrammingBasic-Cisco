#!\bin\python

# El problema en este script es que sobreescribe. La correción está en la version 2.

import os
clear=os.system("clear")
clear=os.system("cls")
clear
file=open("devices.txt","w")

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
