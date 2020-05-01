#!/bin/python 
# @author: [ Paulino Bermúdez R.]
# @Description: Script de conexión automática al Router CSR-1000v.
# Para obtener información del mismo.

import os, json, requests, tabulate, ncclient, urllib3, time 
from netmiko import ConnectHandler
os.system('clear')
os.system('cls')

