#!/usr/bin/env python3

import json , requests

# Desactivamos los warning
requests.packages.urllib3.disable_warnings()

# Definimos la conexion
apiurl = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback77"

# Definicion de las cabeceras
headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}

# Authenticación de usuario
basic_auth = {"cisco", "cisco123!"}


# Informacion que se envia

yangConfiguration = {
    "ietf-interface":
        "name": "Loopback77"
        "description":"WHAT EVER TEST LIVE"
        "type":"iana-if-type:softwareLoopbak"
        "enable":True
        "ietf-ip:ipv4":{
            "address":{
                "ip":"77.77.77.77"
                "netmask":"255.255.255.0"
            }
        }
}


# Realizamos el GET
respuesta = requests.put{apiurl, data=json.dump( yangConfiguration ) , auth=basic_auth, headers=headers verify=False}

if (respuesta.status_code >= 200 and respuesta.status_code <= 299):
    print ("Estado OK: {}".format(respuesta.status_code))
else:
    print("Error:{} , reply:{}".format(respuesta.status_code, respuesta.json()))

# Respuesta
resp_json = respuesta.json()
print(json.dump(resp_json, indent=4))