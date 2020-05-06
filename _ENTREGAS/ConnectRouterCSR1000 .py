#!/bin/python 
# @author: [ Paulino Bermúdez R.]
# @Description: Script de conexión automática al Router CSR-1000v.
# Para obtener información del mismo.

# Librerias importadas
import os, sys, netmiko, json, xml.dom.minidom, requests,tabulate, urllib3, time 
import xml.dom.minidom
from ncclient import manager
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
    print("""
        Hola de nuevo, contarte...
        Tengo almacenados con valores por defecto estos datos:
            - IP: 192.168.56.101
            - Puerto: 22
            - Usuario: cisco
            - Contraseña: cisco123!
        
    """)
    # Default
    ip = "192.168.56.101"
    puerto = 22
    # Usuario
    user = "cisco"
    # Contraseña
    passw = "cisco123!"

    # Validamos datos
    preguntaC = input("¿Son correctos? (Y/N) ")
    preguntaC.upper
    # Pongo las dos opciones porque vi que me fallo 2 veces...por si acaso asi no falla.
    if preguntaC == 'N' or preguntaC == 'n':
        ip = input("IP del dispositivo: ")
        puerto = input("¿Puerto al que conectarse? ")
        print("Credenciales para {:2}.".format(ip))
        user= input("Nombre de usuario: ")
        passw = input("Contraseña: ")
        
    # Conexión SSH al Router.
    print("Espere por favor ... ")
    try:
        os.system("clear")
        os.system("cls")
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
        hostDef='192.168.56.101'
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
            defaultValues = input(" ¿Uso las credenciales por defecto del sistema? (Y/N) (Default:Y)")
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
                descripcion = "AUTO_DESCRIPTION_INTERFACE."
            else:
                descripcion = input("Qué descripción quiere para {}. ".format(nomInter))
            config_commands = [
                'interface {}'.format(nomInter),
                'ip address  {} {}'.format(ipInter,maskInter),
                'description  {}'.format(descripcion)
            ]
            # Output configuration commands.
            output1 = sshCli.send_config_set(config_commands)
            # Sent some simple commands and display the returned output
            print("Config output from the device: \n{}\n".format(output1))
            output2 = sshCli.send_command("show ip int brief")
            print("Print all info: \n")
            print("\n{}\n".format(output2))

        else:
            print("Vale. Vuelvo al menú")
            time.sleep(2)
            os.system('clear')
            os.system('cls')
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
    
    ip = "192.168.56.101"
    portD = 22
    userD = "cisco"
    passwD = "cisco123!"
    masterurl = "https://"+ip+"/restconf/data/ietf-interfaces:interfaces/"
    
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
        username=userD,
        password=passwD
    )
    # Ver interfaces
    output2 = sshCli.send_command("show ip int brief")
    print("_________________________________________")
    print("Estas son las interfaces encontradas: \n{}\n".format(output2))
    print("_________________________________________")
    laborro = input("¿Qué interfaz borro? (Nombre de la interfaz). ")
    url = masterurl+"interface={}".format(laborro)
    print(url ," - COPY")
    # header 
    headers = {
        "Accept":"application/yang-data+json",
        "Content-Type":"application/yang-data+json"
    }
    # Authentication credentiales
    basic_auth = (userD, passwD)
    # Generate connexion
    respuesta = requests.delete(url, auth=basic_auth, headers=headers, verify = False)
    print("PASTED")
    response_json = respuesta.json()
    print(json.dumps(response_json, indent = 2))
    print("_________________________________________")
    print("Estas son las interfaces encontradas: \n{}\n".format(output2))
    print("_________________________________________")

# Método para ver la tabla de rutas.
def table_route():
    print("Crear tabla de rutas")
    # print("Ver ORIGEN - DESTINO -  INTERFAZ DE SALIDA - ")
    # Validación de credenciales
    ip='192.168.56.101'
    port=22
    userD='cisco'
    passwD='cisco123!'
    print("""
    Estos son mis credenciales por defecto:
        IP = {}
        Port = {}
        User = {}
        Password = {}

    """.format(ip,port,userD,passwD))
    correcto = input("¿Son válidas? (Y/N) ")
    if correcto == 'n' or correcto == 'N':
        ip = input("IP: ")
        port = input ("Puerto: ")
        userD = input("Usuario: ")
        passwD = input("Contraseña: ")
    sshCli = ConnectHandler(
        device_type='cisco_ios',
        host=ip,
        port=22,
        username=userD,
        password=passwD
    )
    # Ejecutamps el comando para ver las rutas del Router almacenadas
    output = sshCli.send_command("show ip route")
    print("_________________________________________")
    print("show ip route: \n{}\n".format(output))
    print("_________________________________________")

    # URL a la que me conecto
    url = "https://{}/restconf/data/".format(ip)
    print(url)
    # Credenciales
    basic_auth = ("cisco","cisco123!")

    endpoint = 'Cisco-IOS-XE-native:native'

    headers = {
        'Accept': "application/yang-data+json",
        'Content-Type': "application/yang-data+json"
    }
    
    print("Añadimos la ruta PARA TEST")
    next_hop = "10.0.1.1"
    print(next_hop)
    mask = "255.255.0.0"
    interface = "RouteTest"
    print("""
    Tengo entendido que se quiere es añadir una ruta a otra red, la 10.0.1.0 y que 
    el router que añadiré a la tabla de rutas es: 10.0.1.1 con máscara de subred: 255.255.0.0
    Usaré el serial 1/1/0 del router principal.
    Entonces: 
    """)
    config_commands = [
        "ip route {} {}".format(next_hop,mask),
        "ip route 192.168.56.101 255.255.0.0 serial 1/1/0"        
    ]
    output1 = sshCli.send_config_set(config_commands)
    # Ver de nuevo la tabla  con los cambios
    print("_________________________________________")
    print("show ip route: \n{}\n".format(output))
    print("_________________________________________")

# Modelos YANG
# Ver capabilities
def capabilities():        
    m = manager.connect(
        host="192.168.56.101",
        # Remote port of the NETConf service
        port=830,
        username="cisco",
        password="cisco123!",
        hostkey_verify=False
    )

    print("#Supported Capabilities (YANG models):")
    for capability in m.server_capabilities:
        print(capability)

# Ver todas las itnerfaces de red
def all_interfaces():
    # Create a variable named 'api_url' and assign the URL
    api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"
    # Create the dictionary variable named headers that has keys for Accept and Content-Type
    # Assign the key and values.
    headers = {
        "Accept":"application/yang-data+json",
        "Content-Type":"application/yang-data+json"
    }

    # Create variable authentication
    basic_auth = ("cisco","cisco123!")

    # Send the get request method.
    # Note: Disable verification of the SSL certificate
    resp = requests.get(api_url, auth=basic_auth, headers=headers, verify=False)

    # Evaluate the response
    # Use the YANG model response values can be extracted from the response JSON.
    response_json = resp.json()
    # Verify the code return
    print(response_json)

    # Prettify the output, json.dumps() function with the indent parameters
    read = input("\n Enter to continue ...")
    os.system("clear")
    os.system("cls")
    print(json.dumps(response_json, indent=2))

# ver una interfaz
def una_interface():    
    view_interfaces()
    print(2*"\n")
    estaInter=input("Escriba el nombre de la intrerfaz que desea ver: ") 
    api_url = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface={}".format(estaInter)
    headers = {
        "Accept":"application/yang-data+json",
        "Content-Type":"application/yang-data+json"
    }

    # Create variable authentication
    basic_auth = ("cisco","cisco123!")

    # Exec the delete request method.
    resp = requests.get(api_url, auth=basic_auth, headers=headers,verify=False)
    response_json = resp.json()

    print(json.dumps(response_json, indent=2))

# Método para ver archivos yang Cisco
def get_peticion_yang():
    print("Menú de archivos YANG que ver/configurar.")
    opcion=int(input("""
        OPCIONES DE ARCHIVOS YANG.

        1.) Ver las capabilities del Router Cisco 1000v
        2.) Ver info de las interfaces.
            |
            |-> Ver todas
            |-> Ver una interfaz en concreto
        
        0.) Ir al inicio

        (Seleccione una de las opciones y pulse ENTER.)
        
    """))
    if opcion == 1:
        capabilities()
    elif opcion == 2:
        opcion2 = int(input("""
        Qué opción:
            0. salir
            1. Ver todas
            2. Ver una interfaz en concreto

        """))
        if opcion2 == 0:
            exit
        elif opcion2 == 1:
            all_interfaces()
        elif opcion2 == 2:
            una_interface()
        else:
            print("Esa opción no la entiendo.")
    elif opcion == 0:
        main()
    else:
        print("Esa opción no la entiendo.")

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
            table_route()
        elif opcion == 5:
            print("Selecciono: {}".format(get_peticion_yang))
            get_peticion_yang()
        elif opcion == 0:
            print("Selecciono: {}".format(salir))
            salir()
        elif opcion == None:
            print("Debe ingresar una opción del menú o 0 para salir.")
        else:
            default()
        pausa = input("> Pulse ENTER para continuar")
          
# Ejecución de programa principal
if __name__ == "__main__":
    #main()
    while True:
        try:
            main()       
        except ValueError:
            pausa=input("ALGO HA IDO MAL. VU€lV€ @ 1nT€nT@rl0 --- ENTER para volver a intentarlo.")
            os.system('clear')
            os.system('cls')  
            main()