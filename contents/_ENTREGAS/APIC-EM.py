#!/bin/python 
# @author: [ Paulino Bermúdez R.]
# @Description: 
import os, request, json, time, urllib3 
from tabulate import *
os.system('clear')
os.system('cls')


# Clase principal
class main_API_EM:
    # Defino método de inicio de los objetos de la clase
    def __init__(self):
        # Deshabilito los warning
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
            print("Imposible de resolver: LISTADO DE DEVICES EN RED. - {:2}".format(err))
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



    