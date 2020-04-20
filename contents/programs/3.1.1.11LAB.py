#!/bin/python
import os
os.system("clear")
os.system("cls")

# Using conditional structure
flower=input("Welcome! Enter for start!")
while True:
    flower = input("What is the best plant around the World? ")
    if flower == 'Spathiphyllum':
        print("Yes - Spathiphyllum is the best plant ever!")
        break
    elif flower == 'pelargonium':
        print("Spathiphyllum! Not pelargonium!")
    elif flower == 'spathiphyllum':
        print("No, I want a big Spathiphyllum!")
    else:
        print("Error, this input, I don't process!")
