#!/bin/python 
import os, requests, json, time, re, urllib3, threading
from tabulate import *
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Trace Route IP's
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


def checkStatus(estado,carpeta):
    status = estado
    flowAnalysis = carpeta 

    # Genero un loop para verificar de forma constante el estado del API/flowAnalysis
    count=0
    while status != 'COMPLETED':
        if status == 'FAILED':
            print("Imposible resolver la ruta para esa IP. \n")
            print("Vuelvo al inicio")
            time.sleep(2)
            return
        # Contador de 'saltos' de ruta
        print("Estoy realizando el trabajo...Espere un segundo por favor.")
        time.sleep(1)
        count += 1
        if count > 30:
            print("Ruta inalcanzable. Revise los datos y vuelva a intentarlo de nuevo. ")
            time.sleep(2)
            return
        try:
            # Ruta a la que voy a resolver y analizar
            
            respuesta = get(api="flow-analysis/"+flowAnalysisId)
            resonse_json = respuesta.json()
            print ("Response from GET /flow-analysis/"+flowAnalysisId,json.dumps(response_json,indent=4))
            status = response_json["response"]["request"]["status"]
            print ("Estado: ",status)
        except:
            print("Algo ha fallado para la ruta '{}' compruebe los datos e inténtelo de nuevo. ".format(respuesta))

# Ver en una lista los dispositivos y host para el realizar el path.
def get_DeviceAndHost():
    ipList = []
    try:
        respuesta = (get(api="host"))
        response_json = respuesta.json()
        # Creo un condicional para ir guardando dispositivos en la lista vacia
        # Creo bucle para la lista antes lo inicio a 0
        i = 0
        if response_json["response"] != []:
            for item in response_json["response"]:
                i += 1
                aparatos = [
                    i,
                    "host",
                    item["hostIp"],
                    item["macAddress"]
                ]
                ipList.append(aparatos)
                ident=i
    except:
        print("Falla algo con la IP! Revise los datos y vuelva a intentarlo de nuevo. ")
    return ipList

# Método para la opcion seleccionada por el usuario
def selecciona(prompt, ipList, ident):
    ip =''
    while True:
        entradaPrompt = input(prompt)
        entrada = user_input
        entrada.lower
        if entrada == "q" or entrada == "Q":
            return
        if entrada.isdigit():
            if int(entrada) in range (1, len(ipList)+1):
                ip = ipList[int(entrada)][ident]
                return ip
            else:
                default()

if __name__  == "__main__":
    get_token()
    ipid = 2
    nd_list = get_DeviceAndHost()
    if len(nd_list) < 2:
        print ("Necesito dos valores de entrada: IP de origen e IP de destino.")
        exit
    # Imprimo la lista de aparatos
    print (tabulate(nd_list,headers=['number','type','ip'],tablefmt="rst"))
    # Selecciona los argumentos
    origen_ip = selecciona('Escriba el número de la lista de la IP de origen: ',nd_list,ipid)
    destino_ip = selecciona('Escriba el número de la lista de la IP de destino: ',nd_list,ipid)
            
    path_data = {"sourceIP": origen_ip, "destIP": destino_ip}
    respuesta = request.post(api="flow-analysis",data=path_data)
    response_json = respuesta.json()
    print ("Respuesta del POST /flow-analysis: ",json.dumps(response_json,indent=4))
    try:
        flowAnalysisId = response_json["response"]["flowAnalysisId"]
    except:
        print ("\n He intentado pero me ha sido imposible acceder a 'flowAnalysisId'. ")
        print("Vuelvo al menú principal")
        time.sleep(1)
        exit
    thread = threading.Thread(target=checkStatus, args=('',flowAnalysisId,)) # Passing 
    thread.start()

    ###########################################################
    # Check status of POST /flow-analysis - non-blocking wait #
    ###########################################################
    thread = threading.Thread(target=check_status, args=('',flowAnalysisId,)) # Passing 
    thread.start()