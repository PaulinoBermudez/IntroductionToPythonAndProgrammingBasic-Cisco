mL = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here
#
# USANDO BUCLE Y CONDICIONAL
mL2 = [] # Lista de ayuda temporal
for i in mL:
    if i not in mL2:
        mL2.append(i)
mL = mL2
del mL2
print("The list with unique elements only:")
print("EL EJERCICIO PIDE ESTA OPCION NADA MÁS")
print("1. =>",mL , end="\n")

# USANDO DICCIONARIO
print("PERO TAMBIÉN SON POSIBLES ESTAS OPCIONES")
mL = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista2 = dict.fromkeys(mL).keys()
print("2. =>",lista2, end="\n")

# USANDO COMPARACION DE CONJUNTOS
mL = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista3=list(set(mL))
print("3. =>",lista3, end="\n")

# USANDO COMPRESIÓN DE LISTA (Este fue complejo de entenderlo)
mL = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
d = {}
diccionarioD = [d.setdefault(i,i) for i in mL if i not in d]
print("4. =>",diccionarioD, end="\n")
#
# Básicamente la clave está en que creamos un dicciorio y usamos 
# 'set' para evitar añadir 2 veces el mismo valor 
# Seguidamente, recorremos la lista de elementos mL y sus valores
# los añadimos al diccionario 'd'.
