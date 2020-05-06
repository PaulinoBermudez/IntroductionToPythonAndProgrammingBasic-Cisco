#!/bin/python 
# @author: [ Paulino Bermúdez R.]
# @Description: 
import os, requests, json, time, urllib3, copy
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

# Método de identificador de dispositvo y sus interfaces
def get_interfaces_list():
    #  Estado de solicitud de ticket.
    ticket = get_ticket()
    if ticket == None:
        print(50*"·", "\n NO TIENE TICKET, solicite uno antes o revise la configuración . \n",50*"·")
        return
    else:
        # Ver info de dispositivos en la red
        print("---------- Dispositivos en la red. -------------") 
        mini_net_devices()
        # ¿Qué ID estudiamos?
        nom_select = input("""  0 Salir      
                                
                                INFORMACION DE INTERFACES.
            > Introduzca el 'Host name' o 'IP' del dispositivo que quiere ver. 
            
            (Pulse 'Q' para salir.))
            """)
        nom_select.lower
        if nom_select == 'q' or nom_select == 'Q':
            main()
        
        url=url="https://sandboxapicem.cisco.com/api/v1/interface"
        header = {
            # Método de salida - La pido que sea JSON aunque también puede ser XML (Por ejemplo)
            "Content_type":"application/json",
            # Autenticación
            "X-Auth-Token":ticket
        }
            # Usamos el método GET para obtener la información de interfaces
            # 1- Conexión - Status
        respuesta = requests.get(url, headers=header, verify = False)
        print(50*"·", "\n Status host request: ", respuesta.status_code, "\n", 50*"·")
        try:
            if respuesta.status_code != 200:
                print(" Algo ha salido mal, el estado de su solicitud es: ", respuesta.status_code)
                print("")
                print("Verifique: \n", eval(respuesta.txt)["response"]["detail"], sep="\n")
            else:
                # Creamos el diccionario python de los datos JSON.
                response_json = respuesta.json()
                # La cabecera de la tabla será:
                #
                # + ---------------+------+-----+--------+---------+
                # | Tipo interface | IPv4 | MAC | Puerto |  Status |
                # +----------------+------+-----+--------+---------+
                # Para esto, creamos una lista con estos atributos
                table_header = ["Tipo_Interfaz","IPv4","MAC","Puerto", "Status"]
                # Lista de dispositivos
                interfaceList = []
                for item in response_json["response"]:
                    if item["id"] == nom_select:
                        # Creamos la línea de datos 
                        interface=[
                            item["id"],
                            item["interfaceType"], 
                            item["ipv4Address"], 
                            item["macAddress"], 
                            item["portName"], 
                            item["status"]]
                        interfaceList.append(interface)
                    pausa = input("OJO AL PETARDAZO")
                    return(tabulate(interfaceList, table_header))
        except Exception as err:
            print("Imposible de resolver: LISTADO DE INTERFACES DEL ID {:2}".format(nom_select))
        pausa = input("Pulse ENTER para continuar.")

# Método de rutas de una IP origen a una IP desetino.
def get_path_trace():  
        print("Path trace IP")
        # Estado de solicitud de ticket.
        ticket=get_ticket()
        if ticket == None:
            print(50*"·", "\n NO TIENE TICKET, solicite uno antes o revise la configuración . \n",50*"·")
            return
        else:
            # Solicitamos la info 
            
            # URL de conexión
            url="https://sandboxapicem.cisco.com/api/v1/flow-analysis"
            header = {
                # Método de salida - La pido que sea JSON aunque también puede ser XML (Por ejemplo)
                "Content_type":"application/json",
                # Autenticación
                "X-Auth-Token":ticket
            }
            # Usamos el método GET para obtener la información de los dispositivos conectados.
            respuesta = requests.get(url, headers=header, verify = False)
            print(50*"·", "\n Status host request: ", respuesta.status_code, "\n", 50*"·")
            try:
                if respuesta.status_code != 200:
                    print(" Algo ha salido mal, el estado de su solicitud es: ", respuesta.status_code)
                    print("")
                    print("Verifique: \n", eval(respuesta.txt)["response"]["detail"], sep="\n")
                else:
                    # Ver info de dispositivos en la red
                    print("---------- DISPOSITIVOS DE RED DISPONIBLES. -------------") 
                    get_network_devices_list()         
                    print("---------------------------------------------------------- \n\n")
                    # Preguntamos las IP's de origen y destino de las direcciones deseadas por el usuario
                    verified=False 
                    while True and not verified:
                        source_ip = input("Introduzca la IP de origen del host: ")
                        dest_ip = input("Introduzca la IP de destino del host: ")
                        if source_ip != "" or dest_ip != "":
                            # Creamos un diccionario con los datos del usuario
                            path_data = {
                                "sourceIP":source_ip,
                                "destIP":dest_ip
                            }
                            while not verified:
                                print("Dirección IP del host de origen : " +  path_data['sourceIP'])
                                print("Dirección IP del host de destino: "+ path_data['destIP'], end ="\n")
                                print(50*"·")
                                pausa = input("¿Son correctos los datos? (Y/N)")
                                pausa.lower
                                if pausa == "y":
                                    verified = True 
                                if pausa == "n":
                                    verified = False 
                            continue 
                        else:
                            print("---- ERROR EN LOS DATOS INTRODUCIDOS --- \n Debe escribir una dirección IP para continuar. ")
                            # Volvemos al inicip del while
                            continue 
                    # Iniciamos las pasos de ruta
                    # Convertimos el diccionario path_data con los datos JSON para usarlos en json.dumps()
                    path = json.dumps(path_data)
                    # Solicitamos un ticket a la api 
                    respuesta = requests.post(url, path, headers = header, verify=False)
                    # Vemos el valor que nos devuelve  y lo almacenamos en una variable respuesta_json, comprobamos su analisis ID con los datos almacenados.
                    respuesta_json = respuesta.json()
                    flowAnalysisId = respuesta_json["response"]["flowAnalysisId"]
                    # Vemos los saltos de las rutas, debe terminar con un 'ACCEPTED' si el destino está OK.
                    # URL para añadir los valores que analizar
                    check_url = url+"/"+flowAnalysisId
                    # Iniciamos la variable de estado, pero sin valor por defecto, por si acaso
                    status = ""
                    checks = 1 
                    while status != "COMPLETED":
                        envia = requests.get(check_url, headers= header, verify=False)
                        respuesta_json = envia.json()
                        estado =  respuesta_json["response"]["request"]["status"]
                        # Vemos el resultado de los estados 
                        print("REQUEST STATUS: {:2}".format(status))
                        time.sleep(1)
                        # Nº de iteraciones antes de salir del while.
                        if checks == 15:
                            raise Exception("Número de estados analizados excede el límite. POSIBLE PROBLEMA CON LOS DATOS DE LA RUTA !!! ")
                        elif estado == "FAILED":
                            raise Exception("PROBLEMA CON LOS DATOS DE ENTRADA -- IMPOSIBLE RESOLVER LA RUTA. -> (F)")
                        checks+=1
                    # Mostramos por pantalla el resultado.
                    path_source = respuesta_json["response"]["request"]["sourceIP"]
                    path_dest = respuesta_json["response"]["request"]["destIP"]
                    # Asignamos una lista con las conexiones de respuesta_json
                    networkElemetsInfo = respuesta_json["response"]["networkElemetsInfo"]

                    all_devices=[]
                    device_no = 1

                    # Bucle  retorna la respuesta del JSON y la lista de rutas.
                    for i in networkElemetsInfo:
                        if "name" not in i:
                            name="Unnamed Host"
                            ip = i["ip"]
                            egressInterfaceName = "UNKNOWN"
                            ingressInterfaceName = "UNKNOWN"
                        else:
                            name = i["name"],
                            ip = i["ip"]
                            if "egressInterface" in i:
                                egressInterfaceName = i["egressInterface"]["physicalInterface"]["name"]
                            else:
                                egressInterfaceName = "UNKNOWN"
                            if "ingressInterface" in i:
                                ingressInterfaceName = i["ingressInterface"]["physicalInterface"]["name"]
                            else:
                                ingressInterfaceName = "UNKNOWN"
                        # Creamos una lista de información a la qie mostrar.
                        device = [
                            device_no,
                            name,
                            ip,
                            egressInterfaceName,
                            ingressInterfaceName
                        ]
                        # Añadimos la lista de 'device' en la variable 'all_devices'
                        all_devices.append(device)
                        # Creamos una cadena incremental de nº de dispositivos
                        device_no += 1
                    # Mostramos el origen y destino de las IP's para la traza
                    print("-- Path Trace: -- \n * Source: {:2} \n * Destination: {:2}".format(path_source,path_dest))
                    # Imprimo la lista de dispositivos en la tabla de rutas.
                    print("\t \t Lista de dispositivos \n")
                    table_header = [
                        "Dispositivo",
                        "Nombre",
                        "IP",
                        "Egress Int",
                        "Ingress Int"
                    ]
                    print(tabulate(all_devices, table_header))
            except Exception as err:
                print("Imposible de resolver: LISTADO DE INTERFACES DEL ID {:2}".format(id))
            pausa = input("Pulse ENTER para continuar.")

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