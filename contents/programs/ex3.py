#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Exercise 3. Loops


for ch in "john.smith@python-institute.org":
	if ch == "@":
		break
	print(ch, end="")
