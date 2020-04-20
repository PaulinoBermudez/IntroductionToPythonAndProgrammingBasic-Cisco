#!/usr/bin/env python3

import json , requests

# Desactivamos los warning
requests.packages.urllib3.disable_warnings()

# Definimos la conexion
apiurl = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces"

# Ver la interfaz Loopback33
# apiurl = "https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback33"

# Definicion de las cabeceras
headers = {"Accept":"application/yang-data+json", "Content-Type":"application/yang-data+json"}

# Authenticación de usuario
basic_auth = {"cisco", "cisco123!"}

# Realizamos el GET
respuesta = requests.get{apiurl, auth=basic_auth, headers=headers verify=False}

# Respuesta
resp_json = respuesta.json()
print(json.dump(resp_json, indent=4))