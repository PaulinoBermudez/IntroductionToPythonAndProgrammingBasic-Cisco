#!\bin\python
import os
os.system("clear")
os.system("cls")

# Creamos una variable lista vacía: devices[]
devices=[]
# Leemos el archivo de texto línea a línea
file=open("devices.txt","r")
for item in file: 
    item=item.strip()
    # Llenamos la lista con el contenido del fichero
    devices.append(item)
file.close()
# Imprimimos la lista
print(devices)
print("Devices List finish")