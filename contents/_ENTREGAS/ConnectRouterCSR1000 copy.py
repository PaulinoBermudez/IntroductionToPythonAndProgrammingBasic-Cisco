#!/bin/python 
# @author: [ Paulino Bermúdez R.]
# @Description: Script de conexión automática al Router CSR-1000v.
# Para obtener información del mismo.

# NOTA: NO SE SI PUEDA CONFIGURAR LOE MÉTODOS QUE FALTAN MAÑANA, ASI QUE QUEDA:
#   - métodos de la clase conectaRouter.
#   - probar el script
#   - Ver la información de los archivos YANG.
#   - Redacción del archivo

# Librerias importadas
import os, sys, json, xml.dom.minidom, requests,tabulate, urllib3, time 
from netmiko import ConnectHandler
#from ncclient import manager
# Limpio pantalla del sistema
os.system('clear')
os.system('cls')

# Desactivamos las alarmas de warning del SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Credenciales de inicio y verificación del host - ¿Activo?
def credencial():
    # Solicito los datos necesarios para realizar el menú correctamente
    # IP router
    ip = "192.168.1.137"
    puerto = 22
    print("Credenciales para {:2}.".format(ip))
    # Usuario
    user = "cisco"
    # Contraseña
    passw = "cisco123!"
    # Conexión SSH al Router.
    print("Espere por favor ... ")
    try:
        clienteSSH = ConnectHandler(device_type='cisco_ios', host=ip, port=puerto, username=user, password=passw)
        clienteSSH.disconnect()
        print(30*"___","\n SSH Status Connection - OK.\n",30*"___")
    except Exception as err:
        os.system('clear')
        os.system('cls')    
        print(60*'·')
        print("Imposible conectarse al Router con la IP: {:2} \nCompruebe los datos y vuelva a intentarlo de nuevo.".format(ip))
        print(60*'·')
        sys.exit()
    
# Método para ver las interfaces de red.
def view_interfaces():
    print("Interfaces de red. \n")
    ip = input("IP del router? ")
    # Comando de consola para ver las interfaces de red
    sshCli = ConnectHandler(
     device_type='cisco_ios',
    host=ip,
    port=22,
    username='cisco',
    password='cisco123!'
    )
    # Sent some simple commands and display the returned output
    print("Sendind 'sh ip int brief' ... ")
    output2 = sshCli.send_command("show ip int brief")
    print("show ip int brief: \n{}\n".format(output2))
    print("_________________________________________")
    

# Método para crear una interfaz nueva
def new_interface():
    print("Nueva interfaz de red.")
    # Pedimos los datos necesarios:
    # 1- Tipo de interfaz
    # 2- Nombre de la interfaz
    # 3- IP
    # 4- Máscara de red
    # 5- Descripción de la nueva interfaz
    nueva='y'
    while nueva != 'n':
        hostDef='192.168.1.137'
        puertoDef=22
        userD='cisco'
        passD='cisco123!'

        nueva = input("¿Quiere crear una nueva interfaz?(Y/N) ")
        nueva.lower
        if nueva == "y" or nueva == 'Y':
            print("""
                Valores por defecto. \n
                IP:{}
                Port:{:2}
                User:{}
                Pass:{} 
            """.format(hostDef ,  puertoDef ,  userD , passD))
            defaultValues = input(" ¿Uso las credenciales por defecto del sistema? (Y/N) ")
            defaultValues.lower 
            if defaultValues == 'n' or defaultValues == 'N':
                hostDef=input("IP del host? ")
                puertoDef=input("Puerto: ")
                userD = input("Login User: ")
                passD = input("{} Password: ".format(userD))
            if defaultValues == None:
                print("Uso los Default Values")

            # Conexión SSH             
            sshCli = ConnectHandler(
            device_type='cisco_ios',
            host=hostDef,
            port=puertoDef,
            username=userD,
            password=passD
            )
            # Datos para la nueva interfaz
            print("\n Genial! Ahora los datos de la nueva interfaz. \n")
            nomInter = input(" ¿Qué nombre le ponemos a la interfaz? ")
            ipInter = input(" ¿Qué IP escribo para {} :".format(nomInter))
            maskInter = input(" ¿Máscara para {}? ".format(nomInter)) 
            sino = input(" ¿Escribo una descripión por defecto? (Y/N) ")
            sino.lower
            if sino == 'y' or sino== 'Y':
                descripcion = "AUTO DESCRIPTION INTERFACE."
            else:
                descripcion = input("Qué descripción quiere para {}. ".format(nomInter))
            config_commands = [
                "int "+nomInter,
                "ip address "+ipInter+" "+maskInter,
                "description "+ descripcion
            ]
            # Output configuration commands.
            output1 = sshCli.send_config_set(config_commands)
            output2 = sshCli.send_command("show ip int brief")
            # Sent some simple commands and display the returned output
            print("Config output from the device: \n{}\n".format(output1))
            print("Print all info: \n")
            print("\n{}\n".format(output2))

        else:
            print("Vale. Vuelvo al menú")
            main()

# Método para borrar una interfaz de red del router.
def delete_interface():
    print("Borrar interfaz de red.")
    # Pasos:
    # 0 - Credenciales
    # 1 - Solicito la interfaz que quiero borrar
    # 2 - Creo la cabecera del archivo o headers
    # 3 - Inicio sesion con las credenciales de usuario
    # 4 - Genero la conexión para borrar la interfaz 
    # 5 - Muestro por pantalla el resultado
    
    # Datos por defecto
    
    ip = "192.168.1.137"
    portD = 22
    userD = "cisco"
    passwD = "cisco123!"
    masterurl = "https://"+ip+"/resconf/data/ietf-interfaces:interfaces/"
    
    # Validación de los datos por defecto
    validarIP = input("IP del router {} , es válida? (Y/N) ".format(ip))
    validarIP.upper
    
    # Pongo los dos valores porque (no se el porque, pero no siempre me vale el 'lower'/'upper'
    # para cuidarnos en salud y evitar el fallo... Pongo los dos)
    if validarIP == 'N' or validarIP == 'n':
        ip=input("Escriba la IP correcta: ")
    # Comando de consola para ver las interfaces de red
    sshCli = ConnectHandler(
    device_type='cisco_ios',
    host=ip,
    port=portD,
    user=userD,
    password=passwD
    )
    # Sent some simple commands and display the returned output
    output2 = sshCli.send_command("show ip int brief")
    print("_________________________________________")
    print("Estas son las interfaces encontradas: \n{}\n".format(output2))
    print("_________________________________________")
    laborro = input("¿Qué interfaz borro? ")
    url = masterurl+"interface={}".format(laborro)
    print(url ," - OK")
    # header 
    headers = {
        "Accept":"application/yang-data+json",
        "Content-Tpe":"application/yang-data+json"
    }
    # Authentication credentiales
    basic_auth = (userD, passwD)
    # Generate connexion
    respuesta = requests.delete(url, auth=basic_auth, headers=headers, verify = False)
    response_json = respuesta.json()
    print(json.dumps(response_json, indent = 2))

# Método para ver la tabla de rutas.
def table_route():
    print("Crear tabla de rutas")
    print("Ver ORIGEN - DESTINO -  INTERFAZ DE SALIDA - ")

# Método para ver archivos yang Cisco
def get_peticion_yang():
    print("Menú de archivos YANG que ver/configurar.")

# Defino clase que se ejecuta en caso de seleccionar una opcion inexistente o inválida          
def default():
    print("OPCION INVÁLIDA! - Revise las opciones y vuelva a intentarlo")    

# Función para salir del programa    
def salir():
    os.system('clear')
    os.system('cls')
    print("""
        Finalizado el ConnectRouter CSR 1000v Helper.\n
    
    Espero que mi trabajo te ayude en el tuyo. 
    Los conocimientos adquiridos para crear esta ayuda son gracias a:
    
        PUE- Fundamentos de Python - Devnet y el instructor Iván. --> https://www.pue.es
        Cisco - Becas Digitaliza. Equipo Cisco. --> https://www.netacad.com

    > Es una prueba de modelo, no es mi mejor código pero espero que cumpla con sus requisitos.

    @Paulino E.Bermúdez R.

    \n Adiós!
    """)
    time.sleep(5)
    os.system('clear')
    os.system('cls')
    sys.exit()
     
# Función principal
def main():
    # Inicio la variable opcion
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
    os.system('clear')
    os.system('cls')  
    # Solicitamos datos
    credencial()
    

    while opcion != 0:
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

       
        """)
        
        opcion = int(input("Escriba una opción: "))
        print("\n Escribió: {:2} \n".format(opcion))
        if opcion == 1:
            print("Selecciono: {}".format(view_interfaces))
            view_interfaces()
        elif opcion == 2:
            print("Selecciono: {}".format(new_interface))
            new_interface()
        elif opcion == 3:
            print("Selecciono: {}".format(delete_interface))
            delete_interface()
        elif opcion == 4:
            print("Selecciono: {}".format(table_route))
            table_route
        elif opcion == 5:
            print("Selecciono: {}".format(get_peticion_yang))
            get_peticion_yang()
        elif opcion == 0:
            print("Selecciono: {}".format(salir))
            salir()
        elif opcion == None:
            print("Debe ingresar una opción del menú o 0 para salir.")
        else:
            default
        pausa = input("> Pulse ENTER para continuar")
    
           
# Ejecución de programa principal
if __name__ == "__main__":
    main()