#!/bin/python 
import os, sys, getpass
import math, time

os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Calculadora en Python.
y = input("""
        +-------------------------------------------------+
        |               CALCULADORA PYTHON.               |
        +-------------------------------------------------+
        | Este es un menú de calculadora básica en Python.|
        | contruida por dos funciones:                    |
        |         - MENU()                                |
        |         - OPERA()                               |
        | Para salir del programa, escriba '0'.           |
        |                                                 |
        | @Athor: PAULINO BERMÚDEZ.                       |
        | @Estudio: Becas Digitaliza Cisco. 2019-2020.    |
        |                                                 |
        |         (Pulse ENTER para continuar.)           |
        +-------------------------------------------------+
""") 


def menu():
    os.system('clear')
    os.system('cls')
    # Menú
    username = getpass.getuser()
    print(72*'*')
    print(27*'*',' CALCULADORA ',30*'*')
    print(72*'*')
    print(33*' ','*')
    print(72*'*')
    print("{:2} seleccione una de las opciones: \n".format(username))
    print(72*'_')
    print(22*"_","* Operaciones estándar. ", 24*"_" )
    print(72*'_')
    print("1- Suma \t \t \t         2- Resta")
    print("3- Multiplicación \t \t \t 4- División")
    print("5- Porcentaje \t \t \t \t 6- Exponencial al cuadrado")
    print("7- Exponencial a 'x' \t \t \t 8- Calcular polinomio de primer grado")
    print("9- Polinomio de segundo grado \t \t 10- Raiz cuadrada")
    
    print(72*'_')
    print(22*"_","* Operaciones informáticas. ", 20*"_" )
    print(72*'_')
    print("11- Convertir de decimal a binario \t 12- Convertir de binario a decimal")
    print("13- Convertir de decimal a hexadecimal \t 14- Convertir de decimal a Octal")
    
    print(72*'_')
    print(22*"_","* Operaciones científicas.", 22*"_" )
    print(72*'_')
    print("16- Calcular el log en base 10 de 'X' \t 17- Calcula In de 'X'")
    print("18- Calcular la hipotenusa de un triángulo ")
    print("19- Trigonometría \t \t \t 20- Graficar una función f(x)")
    
    print()
    print("0 -  SALIR. ")
    print()



def opera(y):
    # En caso de ENTER sin número...
    y = int(input("Opción: "))
    print("__________________")
    if y == '*':
        print("Error! Necesito una opción correcta. ") 
    # Árbol condicional de opciones.
    if (y == 0):
        username = getpass.getuser()
        print("Saliendo del programa... Adiós {:2}! ".format(username))
        time.sleep(3)
        os.system('clear')
        os.system('cls')
        sys.exit()
    elif (y==1):
        print("Opción: Suma")
        a=int(input("Introduzca el primer número: "))
        b=int(input("Introduzca el segundo número: "))
        print("\n")
        resultado=(a+b)
        print("El resultado es: ", resultado)
        
    elif (y==2):    
        print("Opción: Resta")
        a=int(input("Introduzca el primer número: "))
        b=int(input("Introduzca el segundo número: "))
        resultado=a-b
        print("El resultado es: ", resultado)
        
    elif (y==3):
        print("Opción: Multiplicación")
        a=int(input("Introduzca el primer número: "))
        b=int(input("Introduzca el segundo número: "))
        resultado=(a*b)
        print("El resultado es: ", resultado)
        
    elif (y==4):
        print("Opción: División")
        a=int(input("Introduzca el primer número: "))
        b=int(input("Introduzca el segundo número: "))
        resultado=(a/b)
        resto=(a%b)
        print("El resultado es: ", resultado, " y de resto: ", resto)
        
    elif (y==5):
        print("Opción: Porcentaje")
        b=int(input("¿Porcentaje? (Número) "))
        a=int(input("¿A qué le calculamos el {:2}% ?: ".format(b)))
        resultado=((a*b)/100)
        print("El ", b,"% de ",a  ," es: ", resultado)
        
    elif (y==6):
        print("Opción: Exponencial al cuadrado")
        a=int(input("Introduzca el número: "))
        resultado=(a**2)
        print("El resultado de {:2} a la '2' es: ".format(a), resultado)
        
    elif (y==7):
        print("Opción: Exponente a la 'x'")
        a=int(input("Introduzca el número natural: "))
        b=int(input("¿A cuánto lo exponemos? "))
        resultado=(a**b)
        print("El resultado de {:2} a la  {:2} es: ".format(a,b), resultado)
        
    elif (y==8):
        print("Opción:Polinomio de primer grado")
        a=int(input("Introduzca valor de las 'X's' : "))
        b=int(input("Introduzca valor de los enteros : "))
        resultado=(b/a)
        print("El resultado de {:2}x+({:2}) = 0, X = ".format(a,b), resultado)
        
    elif (y==9):
        print("Opción: Polinomio de segundo grado")
        a=int(input("Introduzca valor de las 'X^2' : "))
        b=int(input("Introduzca valor de las 'X' : "))
        c=int(input("Introduzca valor de los enteros : "))
        calc = ((b**2)-(4*a*c))
        if calc < 0:
            print(50*"*")
            print("No puedo calular una raiz negativa... Sorry")
            print(50*"*")
        else:
            resultado1=(((-b)+math.sqrt(calc))/(2*a))
            resultado2=(((-b)-math.sqrt(calc))/(2*a))
            print("El resultado para +X de {:2}x^2+({:2}x)+({:2}) = 0 es: ".format(a,b,c), resultado1)
            print("El resultado para -X de {:2}x^2+({:2}x)+({:2}) = 0 es: ".format(a,b,c) , resultado2)
        
    elif (y==10):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)

    elif (y==11):
        print("Opción: DEC a BIN")
        def binario(decimal):
            binario = ''
            while decimal // 2 != 0:
                binario = str(decimal % 2) + binario
                decimal = decimal // 2
            return str(decimal) + binario

        numero = int(input('Introduce el número a convertir a binario: '))
        print(binario(numero))
        
    elif (y==12):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)
        
    elif (y==13):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)
        
    elif (y==14):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)
        
    elif (y==15):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)
    
    elif (y==16):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)
        
    elif (y==17):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)
        
    elif (y==18):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)
        
    elif (y==19):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)
        
    elif (y==20):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)
        
    elif (y==10):
        print("Opción: Raíz cuadrada")
        a=int(input("Introduzca el número: "))
        resultado=(math.sqrt(a))
        print("El resultado es:", resultado)
        
    else:
        print("Número inválido!")
        
if y == 0:
    exit
else:
    while True:  
        menu()
        opera(y)
        pausa=input("Pulse ENTER para continuar.")        
    else:
        pausa=input("ALGO SALIO MAL...F...MAAAALLL!!!")
        exit
    