#!/bin/python 
import os
os.system('clear')
os.system('cls')
import time
# @author: [ Paulino Bermúdez R.]
# @Description: Lab the break statement.
word = ''
print("""

  ,                                         ___                                                   ___   __  
/|   |                                    / (_)                               o                 /   \ /  \ 
 |___|         _  _  _    __,   _  _     |      __   _  _  _     _        _|_     _  _    __,     __/|    |
 |   |\|   |  / |/ |/ |  /  |  / |/ |    |     /  \_/ |/ |/ |  |/ \_|   |  |  |  / |/ |  /  |       \|    |
 |   |/ \_/|_/  |  |  |_/\_/|_/  |  |_/   \___/\__/   |  |  |_/|__/  \_/|_/|_/|_/  |  |_/\_/|/  \___/o\__/ 
                                                              /|                           /|              
                                                              \|                           \|              
""")
time.sleep(3)
while True:
    #os.system('clear')
    #os.system('cls')
    word = input("Write a secret word: ") 
    if word == "chupacabra":
        break
print("""
+_______________________________________________________________+
|______________ You've successfully left the loop ______________|
+_______________________________________________________________+
""")
