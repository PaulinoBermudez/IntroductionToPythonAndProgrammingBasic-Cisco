myList = [10, 8, 6, 4, 2]
del myList[1:3]
print(myList)

print ("______________")

myList = [10, 8, 6, 4, 2]
del myList[:]
print(myList)

print ("______________")

myList = [10, 8, 6, 4, 2]
del myList
print(myList) # El NameError es normal porque se ha borrado en el paso anterior.

print ("______________")
