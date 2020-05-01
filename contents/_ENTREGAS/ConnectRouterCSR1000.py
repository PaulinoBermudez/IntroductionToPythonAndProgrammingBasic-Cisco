#!/bin/python 
# @author: [ Paulino Bermúdez R.]
# @Description: Script de conexión automática al Router CSR-1000v.
# Para obtener información del mismo.

# NOTA: NO SE SI PUEDA CONFIGURAR LOE MÉTODOS QUE FALTAN MAÑANA, ASI QUE QUEDA:
#   - métodos de la clase conectaRouter.
#   - probar el script
#   - Ver la información de los archivos YANG.
#   - Redacción del archivo
import os, sys, json, requests, tabulate, ncclient, urllib3, time 
from netmiko import ConnectHandler
os.system('clear')
os.system('cls')

# Desactivamos las alarmas de warning del SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class inicia:
    conectaRouter(ip,user,key)

class conectaRouter:
    # Definimos los métodos para obtener la información del router
    # Método inicial para las credenciales.
    def __init__(self,ip,user,passw):
        self.host = ip
        self.user = user 
        self.passw = passw
    # Método para ver las interfaces de red.
    def view_interfaces(self):
        print("Interfaces de red.")
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
    def delete_interface(self):
        print("Borrar interfaz de red.")
    def table_route(self):
        print("Crear tabla de rutas")
        print("Ver ORIGEN - DESTINO -  INTERFAZ DE SALIDA - ")
    def yang_files(self):
        print("Menú de archivos YANG que ver/configurar.")
def credencial():
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
            
def default():
    print("OPCION INVÁLIDA! - Revise las opciones y vuelva a intentarlo")
def salir():
    os.system('clear')
    os.system('cls')
    print("Espero que mi trabajo te ayude en el tuyo. \n Adiós!")
    time.sleep(5)
    sys.exit()
def main():
    # Solicitamos datos
    credencial
    opcion = input("""

        Hola y bienvenid@!

        Este es un script de ayuda para sacar información del Router Cisco Serie 1000.
        Las opciones de este script son:
            - Listado de interfaces con información relevante.
            - Creación de interfaces de red.
            - Borrar una interfaz de red.
            - Ver la tabla de rutas.
            - Peticiones a módulos YANG compatibles.
                - Configuración.
                - Obtener información del dispositivo.
        Para ver todos los ejercicios resueltos ver la carpeta  'Model Driven Programmability - DevNet20'

        [ Cuando esté list@ pulse ENTER para continuar.]
        ____________________________________________________________________________________
        @Author: Paulino E. Bermúdez
        - Cisco Netacad: https://www.netacad.com/
        - PUE: https://www.pue.es/
        @Versión: 2020.
    """)
    
    # Creamos un diccionario para el menu de opciones
    opciones = {
        1:api:get_interfaces,
        2:api:add_interfaces,
        3:api:delete_interfaces,
        4:api:routing_table,
        5:api:get_peticion_yang,
        0:salir
    }

    while opcion != 0:
        os.system('clear')
        os.system('cls')
        print("""
        SCRIPT DE AYUDA OBTENER INFO. - Router Cisco 1000v

        Selecciones una de las opciones:
        +_________________________________________________+
        | 1- Ver interfaces red.                          |
        | 2- Crear nueva interfaz de red.                 |
        | 3- Borrar interfaz de red.                      |
        | 4- Ver tabla de rutas guardadas.                |
        | 5- Realizar solitudes a los archivos YANG.      |
        +_________________________________________________+
        | 0- Salir del programa.                          |
        +_________________________________________________+

        (*) Revisar.
        """)
        try:
            opcion = int(input("Escriba una opción: "))
        except:
            dict.get(opcion.default)()
if __name__ == "__main__":
    main()