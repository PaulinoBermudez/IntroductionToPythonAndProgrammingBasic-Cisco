#!/bin/python 
# @author: [ Paulino Bermúdez R.]
# @Description: 
import os, requests, json, time, re, urllib3, threading
from apicem import *
from tabulate import *
os.system('clear')
os.system('cls')


# Defino método de inicio de los objetos de la clase
def __init__():
    # Deshabilito los warning de SSL
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Solicitud de ticket nuevo
# Create the 'get_ticket' function
def get_ticket():
    api_url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "devnetuser",
        "password": "Cisco123!"
    }
    # Send the request
    resp=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)
    #  Print the response and see the status 
    print("______________________________________________________")
    print("Ticket request status: ", resp.status_code)
    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"] 
    print("Your ticket ID is: ", serviceTicket)
    print("______________________________________________________")
    return serviceTicket

# Método para ver los dispositivos existentes en el sistema.            
def  get_hosts_list():
    # Ver estado de solicitud de ticket
    #get_ticket()
    # Solicitamos la info
    url="https://sandboxapicem.cisco.com/api/v1/host"
    ticket = get_ticket()
    header = {
        # Método de salida - La pido que sea JSON aunque también puede ser XML (Por ejemplo)
        "Content_type":"application/json",
        # Autenticación
        "X-Auth-Token": ticket
    }

    # Usamos el método GET para obtener la información de los hosts existentes.
    respuesta = requests.get(url, headers=header, verify = False)
    print(50*"·", "\n Status host request: ", respuesta.status_code, "\n", 50*"·")
    
    if respuesta.status_code != 200:
        print(" Algo ha salido mal, el estado de su solicitud es: ", respuesta.status_code)
        print("")
        raise Exception("Status code does not equal 200. Response text: " + respuesta.text)
    
    # Creamos el diccionario python de los datos JSON.
    response_json = respuesta.json()
    # Lista de hosts
    hostList = []
    i = 0
    for item in response_json["response"]:
        # Sumámos +1 a la lista de hosts
        i += 1
        # Añadimos los datos de host a la lista hostList.
        # 1- Creamos el objeto con los datos
        # 2- Lo añadimos  a la lista 'hostList' con .append
        hostX=[i,
            item["hostIp"], 
            item["hostMac"], 
            item["hostType"], 
            item["connectedNetworkDeviceIpAddress"], 
            item["id"]]
        hostList.append(hostX)
    # La cabecera de la tabla será:
    #
    # + ---+-----+-----+--------------+---------------------+----+
    # | Nº |  IP | MAC | Tipo de host | IP disp. conectado  | ID |
    # +----+-----+-----+--------------+---------------------+----+
    # Para esto, creamos una lista con estos atributos
    table_header = ["Numero","  IP  "," MAC "," Tipo de host    ", "    IP disp. conectado  ", "ID"]    
    print(tabulate( hostList, table_header))
    
# Método para ver los dispositivos en red conectados.
def get_network_devices_list():
    # Estado de solicitud de ticket.
    ticket = get_ticket()
    if ticket == None:
        print(50*"·", "\n NO TIENE TICKET, solicite uno antes o revise la configuración . \n",50*"·")
        return
    # Solicitamos la info
    url="https://sandboxapicem.cisco.com/api/v1/network-device"
    header = {
        # Método de salida - La pido que sea JSON aunque también puede ser XML (Por ejemplo)
        "Content_type":"application/json",
        # Autenticación
        "X-Auth-Token":ticket
    }

    # Usamos el método GET para obtener la información de los dispositivos conectados.
    respuesta = requests.get(url, headers=header, verify = False)
    os.system("clear")
    os.system("cls")

    print(50*"·", "\n Status host request: ", respuesta.status_code, "\n", 50*"·")
    print("Status of /host request: ", respuesta.status_code)
    if respuesta.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + respuesta.text)
    response_json = respuesta.json()


    # Parse and format the JSON response data
    # Create a new list
    devices_list = []

    # Generate the for loop to create a list
    i = 0
    for item in response_json["response"]:
        i+=1
        host = [
                i,
                item["id"],
                item["hostname"],
                item["managementIpAddress"],
                item["macAddress"], 
                item["serialNumber"],
                item["family"],
                item["role"]
                ]
        devices_list.append(host)
    table_header = ["Number", "ID","Host name","IP Address", "MAC Address", "S/N", "Family", "Rol"]
    print( tabulate(devices_list, table_header) )

def mini_net_devices():
    # Estado de solicitud de ticket.
    ticket = get_ticket()
    if ticket == None:
        print(50*"·", "\n NO TIENE TICKET, solicite uno antes o revise la configuración . \n",50*"·")
        return
    # Solicitamos la info
    url="https://sandboxapicem.cisco.com/api/v1/network-device"
    header = {
        # Método de salida - La pido que sea JSON aunque también puede ser XML (Por ejemplo)
        "Content_type":"application/json",
        # Autenticación
        "X-Auth-Token":ticket
    }

    # Usamos el método GET para obtener la información de los dispositivos conectados.
    respuesta = requests.get(url, headers=header, verify = False)
    os.system("clear")
    os.system("cls")

    if respuesta.status_code != 200:
        raise Exception("Status code does not equal 200. Response text: " + respuesta.text)
    response_json = respuesta.json()


    # Parse and format the JSON response data
    # Create a new list
    devices_list = []

    # Generate the for loop to create a list
    i = 0
    for item in response_json["response"]:
        i+=1
        host = [
                i,
                item["id"],
                item["hostname"],
                item["managementIpAddress"],
                item["family"],
                item["role"]
                ]
        devices_list.append(host)
    table_header = ["Number", "ID","IP Add", "Host name", "Family ", "Role"]
    print("""               DATA DEVICES INFO""")
    print( tabulate(devices_list, table_header) )

# Peticion de un token rapido -- Se puede eliminar si modificamos la get_ticket
def get_token():
    url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    credenciales = {
        "username":"devnetuser",
        "password":"Cisco123!"
    }
    header = {
        "Content-Type":"application/json"
    }
    response = requests.post(url,data=json.dumps(credenciales), headers = header, verify = False).json()
    return response["response"]["serviceTicket"]

# Método para ver la configuracion que está corriendo en los dispositivos actuales, con 1 parametro
def get_config_run():
    print("""
                HOLA! 
                Comentarte una  cosilla, para esta parte generaré un archivo con toda la 
                configuración.
                Estará en el directorio actual de trabajo y es de formato txt.

                Para un reconocimiento fácil lo llamaré: __CONFIGURACION_'device'+'hora'__.txt
    

    """)
    # Pido ticket
    url = "https://sandboxapicem.cisco.com/api/v1/ticket"
    credenciales = {
        "username":"devnetuser",
        "password":"Cisco123!"
    }
    header = {
        "Content-Type":"application/json"
    }
    response = requests.post(url,data=json.dumps(credenciales), headers = header, verify = False).json()
    token = response["response"]["serviceTicket"]
    print(token)
    # pausa = input("ENTER para continuar")
    # Header
    header = {
        # Autenticación
        "X-Auth-Token":token
    }
    
    # URL de consulta
    url="https://sandboxapicem.cisco.com/api/v1/network-device/config"
    
    # Realizo la consulta y lo guardo en formato JSON
    response = requests.get(url, headers=header, verify=False).json()
    # Genero un bucle que guarde la configuración que saca la consulta anterior
    count=1
    for data in response["response"]:
        # Variables par alos nombres del fichero
        fecha = time.strftime("%H.%M.%S")
        device = re.findall('hostname\s(.+?)\s', data['runningConfig'])[0]
        # Fichero
        filename="__CONFIGURACION__{:}_{:}.txt".format(device,fecha)
        # Creo un fichero txt (temporal) en el directorio actual
        file = open(filename, 'w')
        # Escribo los datos de configuracion 'en funcionamiento' dentro del fichero 'file'
        file.write(data['runningConfig'])
        # Cierro el fichero con los datos almancenados
        file.close()
        count+=1
        print("Fichero creado... Para ver la información consulte el fichero {}".format(filename))
    print("Aquí el fichero.")    
    conf = open(filename)
    conf.read()

# Verificacion del estado de la API
def checkStatus(a1,a2):
    status = a1
    flowAnalysis = a2 

    # Genero un loop para verificar de forma constante el estado del API/flowAnalysis
    count=0
    while status != 'COMPLETED':
        if status == 'FAILED':
            print("Imposible resolver la ruta para esa IP. \n")
            print("Vuelvo al inicio")
            time.sleep(2)
            main()
        



# Método de rutas de una IP origen a una IP desetino.
def get_path_trace():  
        pausa = input("""       Path trace IP 
        
            Esta parte del script es un poco más completa ya que aquí reuno varias verificaciones del API.
            (Compleja para mi cuando me lié a hacerlo claro...)

            Veo:
                - Host()
                - Network-Device()
                - Flow-analysis()
                - Flow-analysis/{flowAnalysysId}

            Seguí la ayuda de: https://developer.cisco.com/site/apic-em-rest-api/
            
            Espero que sea de su gusto y pulse ENTER para continuar.
        """)
       
# Función que 'salta' en caso de que la opción introducida por el usuario sea inválida.
def default():   
    print("ERROR!", "La opción introducida no es válida. Vuelva a intentarlo de nuevo. [Escribir nº de opción del menú]")

# Función de final de programa
def finalizar():   
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)    
    print("""
                Fin del programa
        Gracias por usar el programa de APIC-EM. 
       
        @Paulino E. Bermúdez R. 
        \n 
        @Version: Becas_Digitaliza:2019-2020 \n
        {:2}
    """.format(current_time))
    time.sleep(3)
    os.system('clear')
    os.system('cls')
    exit()
# Funcion principal del programa
def main():
    t = time.localtime()
    # autoToken = get_token()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    
    # Inicio la variable de selección
    opcion = input("""HOLA y Bienvenid@s!
        
        Este es el programa de automatización del controlador APIC-EM de Cisco.
        Lea detenidamente esta pantalla para tener una idea de lo que encontrará.

        Datos importantes usados.
            - Antes de empezar:
                - URL: https://sandboxapicem.cisco.com/api/'x' <-- Varía según la 
                                                                                info solicitada
                - Usuario: devnetuser.
                - Contraseña: Cisco123!
            - Formato de salida de los datos:
                - JSON
        
        
        [ Cuando esté list@ pulse ENTER para continuar.]
        ____________________________________________________________________________________
        @Author: Paulino E. Bermúdez
        - Cisco Netacad: https://www.netacad.com/
        - PUE: https://www.pue.es/
        @Versión: 2020.
    
    """)
    os.system('clear')
    os.system('cls')
   
    # Bucle del menú de opciones
    while True:
        print("""{}
            APIC-EM AUTOMATIZADA.

        Selecciones una de las opciones:
        +___________________________________________________+
        | 1- Crear ticket nuevo.                            |
        | 2- Host de la red.                                |
        | 3- Dispositivos en la red.                        |
        | 4- Config. en ejecución de los dispositivos en red|
        | 5- Trazado de ruta. *                             |
        +___________________________________________________+
        | 0- Salir del programa.                            |
        +___________________________________________________+
        
        (*) Revisar.
        """.format(current_time))
        opcion = int(input("Seleccione una de las opciones del menú: "))
            
        try:
            if opcion == 1:
                print("Selecciono: {}".format(get_ticket))
                get_ticket()
            elif opcion == 2:
                print("Selecciono: {}".format(get_hosts_list))
                get_hosts_list()
            elif opcion == 3:
                print("Selecciono: {}".format(get_network_devices_list))
                get_network_devices_list()
            elif opcion == 4:
                print("Selecciono: {}".format(get_config_run))
                get_config_run()
            elif opcion == 5:
                print("Selecciono: {}".format(get_path_trace))
                get_path_trace()
            elif opcion == 0:
                print("Selecciono: {}".format(finalizar))
                finalizar()
            else:
                default()
            pausa = input("> Pulse ENTER para continuar")    
        except ValueError:
            default()
            print("Debe ingresar una opción del menú o 0 para salir.")
                       

# Programa principal
if __name__ == "__main__":
    main()