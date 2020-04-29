#!/bin/python 
import os
os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: What is the output of the following snippet?

lst = [1, 2, 3, 4, 5]
# Insert in:
# Position: 1
# Value: 6
lst.insert(1, 6)
print("Insert ",lst)
# Delete 1st element
del lst[0]
print("Delete ",lst)
# Add (in final) value 1 at list
lst.append(1)

print("Append ", lst) # 6,2,3,4,5,1