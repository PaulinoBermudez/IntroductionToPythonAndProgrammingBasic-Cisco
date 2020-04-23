#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Drop the vowels at word.

# Prompt the user to enter a word and assign it to the userWord variable.
print("""
Hello and welcome! 

In this case, you need write a one word and I must drop the vowels...
--> If you want to finished, use the 'Q' letter.
Well! go on! \n
""")

# Define a variables
vowels="AEIOU" # IN THIS CASE, I AMN'T NEED MINUSCULE VOWELS BECAUSE THE WORD IS UPPER.
while True:
    userWord = input("Write a word: ")

    if userWord != 'Q' or userWord != 'q':
        # Change the input word in upper word.
        userWord = userWord.upper()

        # Print the word
        print(32*"__")
        print(userWord)
        print(32*"__")

        # Search Looping vowels
        for letter in userWord:
            # Complete the body of the for loop.
            # The function 'in', look the content at constant in a variable
            if letter in vowels:
                continue
            else:
                print(letter)


        print(40*"=","Method 2")
        # Method 2 -  Not good but... is a initial code
        for letter in userWord:
            if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
                continue
            else:
                print(letter)
    else:
        break