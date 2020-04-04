#!/bin/python

import urllib.parse
import requests
import os
os.system("clear")
os.system("cls")
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
    # Especificamos el punto de partida y destino 
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
    json_data = requests.get(url).json()

# 
# Print the URL and check the status of the JSON request.
# * Add the statements below, which will do the following:
#    -   Print the constructed URL so that the user can see the exact request made by he application.
#    -   Parse the JSON data to obtain the status code value.
#    -   Start an if loop that chechs for as successful call, which a value of 0. Add a print statement to display the statuscode value and its meaning. 
#    The \n adds a blank line below the output.
# 
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("_________________________________________________")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " +  (json_data["route"]["formattedTime"]))
        print("Miles: " + str(json_data["route"]["distance"]))
        print("Fuel used (Gal): " + str(json_data["route"]["fuelUsed"]))
        print("_________________________________________________")

    if json_status == 0:
        print("API status: " + str(json_status) + " = A successful route call. \n")