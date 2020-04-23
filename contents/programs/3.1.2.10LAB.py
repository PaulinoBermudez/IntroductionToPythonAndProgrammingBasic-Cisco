#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Drop the vowels at word.

# Prompt the user to enter a word and assign it to the userWord variable.
print("Hello and welcome! In this case, you need write a one word and I must drop the vowels...Well! go on! \n")
userWord = input("Write a word")
for letter in userWord:
    # Complete the body of the for loop.
    if 