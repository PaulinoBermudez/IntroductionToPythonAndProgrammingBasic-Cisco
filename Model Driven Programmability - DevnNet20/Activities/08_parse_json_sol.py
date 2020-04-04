#!/bin/python

import urllib.parse
import requests

''' 
 * Lab - Parsing JSON with a Python Application
 * Objectives:
 *  - Obtain a MapQuest API key.
 *  - Import necessary modules.
 *  - Create API request variables and construct a URL.
 *  - Add user input functionality.
 *  - Add a quit feature so that the user can end the application.
 *  - Display trip information for time, distance and fuel usage.
 *  - Iterate through the JSON data to extract and output the directions.
 *  - Display error messages for invalid user input.
 '''

# Creamos las variables 

# main_api aquí se agrega la URL principal a la que se está accediendo.
main_api = "https://www.mapquestapi.com/directions/v2/route?"
# Especificamos el punto de partida
orig = "Washington"
# Especificamos el punto de destino
dest = "Chicago"
# Clave del consumidor que recupere del sitio web para desarrolladores.
key = "AwAipWaBJZPU6yoS7BUJMFrqMxjQEW8u"

'''
    La autenticación de una solicitud RESTful se realiza de una de las cuatro maneras posibles:
        - Ninguno: El recurso API es público y cualquiera puede realizar la solicitud. 
        - HTTP básico: El nombre de usuario y la contraseña se pasan al servidor en una cedena codificada. Este método es menos común que el Token y la autenticación OAuth.
        - Token: Una clave secreta generalmente recuperada del portal para desarrolladores de API web.
        - Autorización abierta (OAuth): Un estándar para recuperar un token de acceso de un proveedor de identidad. El token se pasa con cada llamada a la API.
'''

# URL se combina con las cuatro variables anteriores para dar formato a la url solicitada agregando l método urlencode.
url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})

json_data = requests.get(url).json()
print(json_data)
