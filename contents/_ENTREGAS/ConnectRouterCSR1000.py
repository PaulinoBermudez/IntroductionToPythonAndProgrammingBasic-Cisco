#!/bin/python 
# @author: [ Paulino Bermúdez R.]
# @Description: Script de conexión automática al Router CSR-1000v.
# Para obtener información del mismo.

import os, sys, json, requests, tabulate, ncclient, urllib3, time 
from netmiko import ConnectHandler
os.system('clear')
os.system('cls')

# Desactivamos las alarmas de warning del SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class conectaRouter:
    # Definimos los métodos para obtener la información del router
    # Método inicial para las credenciales.
    def __init__(self,ip,user,passw):
        self.host = ip
        self.user = user 
        self.passw = passw
    # Método para crear una interfaz nueva
    def new_interface(self):
        # Pedimos los datos necesarios:
        # 1- Tipo de interfaz
        # 2- Nombre de la interfaz
        # 3- IP
        # 4- Máscara de red
        # 5- Descripción de la nueva interfaz
        while True:
            # URL de conexión al Router
            url = "https://"+self.host+"/resconf/data/ietf-interfaces:interfaces"
            # Pedimos los datos de la nueva interfaz
            name = input("¿Qué nombre asigno a la nueva interfaz? ")
            ip = input("¿Qué IP assigno a la interfaz? ")
            mask = input("¿Qué máscara de red tiene la interfaz? ")
            add = input("¿Añadimos algo de descripción? (Y/N) - Sino, añado una por default: ")
            add.lower
            if add == 'Y':
                description = input("¡Cuéntame! ¿Qué descripción añado? ")
            else:
                description = "Interfaz: {:2}-{:2}/{:2}".format(name,ip,mask)
                print("Descripción por defaut: {:2}".format(description))
            # Creamos la nueva interfaz
            conecta = url+"/interface="+name
            print("\n URL a la que nos conectamos es: {:2}".format(conecta)+"\n\n")
            # Cabecera de la aplicación.
            cabecera = {
                # Tipo de dato con el que trabajamos: yang+json
                "Accept":"application/yang-data+json",
                "Content-type:":"application/yang-data+json"
            }
            # Authentication: User + Password method
            basicAuth = (self.user, self.passw)

def main():
    # Solicito los datos necesarios para realizar el menú correctamente
    # IP router
    ip = input("Introduzca la dirección IP del Router Cisco 1000v: ")
    puerto = int(input("Puerto de conexión: (En mi caso: 830, por default: 22) "))
    print("Credenciales para {:2}.".format(ip))
    # Usuario
    user = input ("Introduzca el usuario login del sistema: ")
    # Contraseña
    key = input ("Introduzca la contraseña de acceso: ")
    # Conexión SSH al Router.
    try:
        clienteSSH = ConnectHandler(device_type='cisco_ios', host=ip, port=puerto, username=user, password=key)
        clienteSSH.disconnect()
    except Exception as err:
        print("Imposible conectarse al Router con la IP: {:2} \nCompruebe los datos y vuelva a intentarlo de nuevo.".format(ip))
        sys.exit()

    conectaRouter = conectaRouter(ip,user,key)

    init = conectaRouter

if __name__ == "__main__":
    