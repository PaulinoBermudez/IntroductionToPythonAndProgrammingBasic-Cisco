# Primera parte
myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]
for i in myList:
    if i > largest:
        largest = i
print(largest)
print(5*"___")
# Segunda parte -   parte de código.
myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]
for i in range(1, len(myList)):
    if myList[i] > largest:
        largest = myList[i]
print(largest)
print(5*"___")

# Tercera parte
myList = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = myList[0]
for i in myList[1:]:
    if i > largest:
        largest = i
print(largest)
print(5*"___")
