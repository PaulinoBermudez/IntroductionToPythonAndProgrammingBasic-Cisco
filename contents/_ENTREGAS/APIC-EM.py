#!/bin/python 
# @author: [ Paulino Bermúdez R.]
# @Description: 
import os, requests, json, time, urllib3
from tkinder import MessageBox
from tabulate import *
os.system('clear')
os.system('cls')


# Clase principal
class class_API_EM:
    # Defino método de inicio de los objetos de la clase
    def __init__(self):
        # Deshabilito los warning de SSL
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.ticket = None
    # Método para obtener ticket de acceso a la plataforma APIC-EM
    def get_ticket(self):
        # URL de acceso
        url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
        # Cabecera
        header = {
            # Tipo de contenido 
            "Content-Type":"application/json"
        }
        # Credenciales
        credentials = {
            "password":"Xj3BDqbU",
            "username":"devnetuser"
        }
        # Solicitamos un ticket
        respuesta =  requests.post(url,json.dumps(credentials), header=header, verify = False)
        # Vemos el estado de la petición
        # Estado 200: OK!
        # Estado 202: Accepted.
        if (respuesta.status_code == 200 ) or ( respuesta.status_code == 202):
            # Creamos diccionario de los datos JSON de la API
            response_json = respuesta.json()
            self.ticket = response_json['response']['serviceTicket']
            print(50*"·", "\n Su ticket. \n- Status: OK!")
            print("- Identificador de ticket: ", self.ticket ,"\n", 50*"·")
            pausa = input("Pulse ENTER para continuar")
        else:
            print(50*"·", "Su ticket. \n- Status: Fail!")
            pausa = input("Pulse ENTER para continuar")
    # Método para ver los dispositivos existentes en el sistema.            
    def  get_hosts_list(self):
        # Ver estado de solicitud de ticket
        if self.ticket == None:
            print(50*"·", "\n NO TIENE TICKET, solicite uno antes. \n",50*"·")
            return
        # Solicitamos la info
        url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
        header = {
            # Método de salida - La pido que sea JSON aunque también puede ser XML (Por ejemplo)
            "Content_type":"application/json",
            # Autenticación
            "X-Auth-Token":self.ticket
        }

        # Usamos el método GET para obtener la información de los hosts existentes.
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
                # + ---+-----+-----+--------------+---------------------+----+
                # | Nº |  IP | MAC | Tipo de host | IP disp. conectado  | ID |
                # +----+-----+-----+--------------+---------------------+----+
                # Para esto, creamos una lista con estos atributos
                table_header = ["Num","IP","MAC","Tipo de host", "IP disp. conectado", "ID"]
                # Lista de hosts
                hostList = []
                for item in response_json["response"]:
                    # Sumámos +1 a la lista de hosts
                    i += 1
                    # Añadimos los datos de host a la lista hostList.
                    # 1- Creamos el objeto con los datos
                    # 2- Lo añadimos  a la lista 'hostList' con .append
                    hostList.append([i, item["hostIp"], item["hostMac"], item["hostType"], item["connectedNetworkDeviceIpAddress"], item["id"]])
                host_list_print = "\n".join(str(x) for x in hostList)
                host_list_print = host_list_print.replace("u'", "'")
                host_list_print = host_list_print.replace("[", "")
                host_list_print = host_list_print.replace("]", "")
                host_list_print = host_list_print.replace("'", "")
                pausa = input("OJO AL PETARDAZO")
                return(tabulate(host_list_print, table_header))
        except Exception as err:
            print("Imposible de resolver: LISTADO DE HOST EN EL SISTEMA. - {:2}".format(err))
        pausa = input("Pulse ENTER para continuar.")
    # Método para ver los dispositivos en red conectados.
    def get_network_devices_list(self):
        # Estado de solicitud de ticket.
        if self.ticket == None:
            print(50*"·", "\n NO TIENE TICKET, solicite uno antes. \n",50*"·")
            return
        # Solicitamos la info
        url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
        header = {
            # Método de salida - La pido que sea JSON aunque también puede ser XML (Por ejemplo)
            "Content_type":"application/json",
            # Autenticación
            "X-Auth-Token":self.ticket
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
                # Creamos el diccionario python de los datos JSON.
                response_json = respuesta.json()
                # La cabecera de la tabla será:
                #
                # + ---+-----------+-----+--------------+------+----+
                # | Nº |  hostname | MAC | instanceUuid | ROLE | ID |
                # +----+-----------+-----+--------------+------+----+
                # Para esto, creamos una lista con estos atributos
                table_header = ["Num","Host_Name","MAC","Instance uid", "Role", "ID"]
                # Lista de dispositivos
                deviceList = []
                for item in response_json["response"]:
                    # Sumámos +1 a la lista de dispositivos
                    i += 1
                    # Añadimos los datos de 'device' a la lista deviceList.
                    # 1- Creamos el objeto con los datos
                    # 2- Lo añadimos  a la lista 'deviceList' con .append
                    deviceList.append([i, item["hostname"], item["macAddress"], item["instanceUuid"], item["role"], item["id"]])
                network_list_print = "\n".join(str(x) for x in deviceList)
                network_list_print = network_list_print.replace("u'", "'")
                network_list_print = network_list_print.replace("[", "")
                network_list_print = network_list_print.replace("]", "")
                network_list_print = network_list_print.replace("'", "")
                pausa = input("OJO AL PETARDAZO")
                return(tabulate(network_list_print, table_header))
        except Exception as err:
            print("Imposible de resolver: LISTADO DE DISPOSITIVOS EN RED. - {:2}".format(err))
        pausa = input("Pulse ENTER para continuar.")
    # Método de identificador de dispositvo y sus interfaces
    def get_interfaces_list(self):
        #  Estado de solicitud de ticket.
        if self.ticket == None:
            print(50*"·", "\n NO TIENE TICKET, solicite uno antes. \n",50*"·")
            return
        else:
            # Ver info de dispositivos en la red
            print("---------- Dispositivos en la red. -------------") 
            self.get_network_devices_list()
            # ¿Qué ID estudiamos?
            id_select = input("""       INFORMACION DE INTERFACES.
                > Introduzca el ID del dispositivo del que quiere ver sus interfaces de red: 
                
                (Pulse 'Q' para salir.)
                """)
            id_select.lower
            if id_select == 'q':
                return
            else:
                url=url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/interface"
                header = {
                    # Método de salida - La pido que sea JSON aunque también puede ser XML (Por ejemplo)
                    "Content_type":"application/json",
                    # Autenticación
                    "X-Auth-Token":self.ticket
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
                            if item["deviceId"] == id_select:
                                # Creamos la línea de datos 
                                interfaceList.append([item["interfaceType"], item["ipv4Address"], item["macAddress"], item["portName"], item["status"]])
                            interface_list_print = "\n".join(str(x) for x in deviceList)
                            interface_list_print = interface_list_print.replace("u'", "'")
                            interface_list_print = interface_list_print.replace("[", "")
                            interface_list_print = interface_list_print.replace("]", "")
                            interface_list_print = interface_list_print.replace("'", "")
                            pausa = input("OJO AL PETARDAZO")
                            return(tabulate(interface_list_print, table_header))
                except Exception as err:
                    print("Imposible de resolver: LISTADO DE INTERFACES DEL ID {:2}".format(id_select))
                pausa = input("Pulse ENTER para continuar.")
    # Método de rutas de una IP origen a una IP desetino.
    def get_path_trace(self):  
        print("Path trace IP")
        # Estado de solicitud de ticket.
        if self.ticket == None:
            print(50*"·", "\n NO TIENE TICKET, solicite uno antes. \n",50*"·")
            return
        else:
            # Solicitamos la info 
            
            # URL de conexión
            url="https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis"
            header = {
                # Método de salida - La pido que sea JSON aunque también puede ser XML (Por ejemplo)
                "Content_type":"application/json",
                # Autenticación
                "X-Auth-Token":self.ticket
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
                    self.get_network_devices_list()                    
                    # Creamos el diccionario python de los datos JSON.
                    response_json = respuesta.json()
                        

# Función que 'salta' en caso de que la opción introducida por el usuario sea inválida.
def default():   
    root =  tkinter.Tk()
    root.withdraw()

    MessageBox.showinfo("ERROR!", "La opción introducida no es válida. Vuelva a intentarlo de nuevo. [Escribir nº de opción del menú]")
# Función de final de programa
def finalizar():   
    root =  tkinter.Tk()
    root.withdraw()

    MessageBox.showinfo("Fin del programa", "Gracias por usar el programa de APIC-EM. Un 10 no estaría mal. :sweat_smile: \n @Version: Becas_Digitaliza:2019-2020")
# Funcion principal del programa
def main():
    # Invoco la clase principal del programa
    api = class_API_EM()
    # Inicio la variable de selección
    opcion = input("""
        HOLA y Bienvenid@s!
        
        Este es el programa de automatización del controlador APIC-EM de Cisco.
        Lea detenidamente esta pantalla para tener una idea de lo que encontrará.

        Datos importantes usados.
            - Antes de empezar:
                - URL: https://devnetsbx-netacad-apicem-3.cisco.com/api/'x' <-- Varía según la 
                                                                                info solicitada
                - Usuario: devnetuser.
                - Contraseña: Xj***bU
            - Formato de salida de los datos:
                - JSON
        
        
        [ Cuando esté list@ pulse ENTER para continuar.]
        ____________________________________________________________________________________
        @Author: Paulino E. Bermúdez
        - Cisco Netacad: https://www.netacad.com/
        - PUE: https://www.pue.es/
        @Versión: 2020.
    
    """)
    # Creamos un diccionario para el menu de opciones
    opciones = {
        1:api:get_ticket,
        2:api:get_hosts_list,
        3:api:get_network_devices_list,
        4:api:get_interfaces_list,
        0:finalizar
    }

    # Bucle del menú de opciones
    while opcion != 0:
        os.system('clear')
        os.system('cls')
        print("""
            APIC-EM AUTOMATIZADA.

        Selecciones una de las opciones:
        +_________________________________________________+
        | 1- Crear ticket nuevo.                          |
        | 2- Host de la red.                              |
        | 3- Dispositivos en la red.                      |
        | 4- Ver interfaces de red de un dispositivo (ID) |
        +_________________________________________________+
        | 0- Salir del programa.                          |
        +_________________________________________________+
        """)
        try:
            opcion = int(input("Escriba una opción: "))
        except:
            dict.get(opcion.default)()
if __name__ == "-_main__":
    main()

