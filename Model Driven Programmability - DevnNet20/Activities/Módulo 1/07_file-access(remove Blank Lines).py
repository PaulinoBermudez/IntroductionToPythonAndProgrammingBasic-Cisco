#!\bin\python
import os
os.system("clear")
os.system("cls")

# Creamos el fichero e introducimos la primera línea
file = open("devices.txt","w")
file.write("Cisco 819 Router \n" + os.linesep)
print("Devices written")
file.close()
# Escribimos el resto de las filas
file = open("devices.txt","w")
file.write("Cisco 881 Router \n")
file.write("Cisco 888 Router \n")
file.write("Cisco 1100 Router \n")
file.write("Cisco 4321 Router \n")
file.write("Cisco 4331 Router \n")
file.write("Cisco 4351 Router \n")
file.write("Cisco 2960 Catalyst Switch \n")
file.write("Cisco 3850 Catalyst Switch \n")
file.write("Cisco 7700 Nexus Switch \n")
file.write("Cisco Meraki MS220-8 Cloud Managed Switch \n")
file.write("Cisco Meraki MX64W Security Appliance \n")
file.write("Cisco Meraki MX84 Security Appliance \n")
file.write("Cisco Meraki MC74 VoIP Phone \n")
file.write("Cisco 3860 Catalyst Switch \n")
file.close()
# Leemos el archivo de texto línea a línea
file=open("devices.txt","r")
for item in file: 
    item=item.strip()
    print(item)
file.close()
print("Devices List finish")