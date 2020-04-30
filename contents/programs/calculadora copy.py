#!/bin/python 
import os, sys, getpass, platform
import math, time

os.system('clear')
os.system('cls')
# @author: [ Paulino Bermúdez R.]
# @Description: Calculadora en Python.
pythonv = platform.python_version()
sist = platform.platform()
y = input("""
        +------------------------------------------------------------------+
        |               CALCULADORA PYTHON.                                |
        +------------------------------------------------------------------+
        | Este es un menú de calculadora básica en Python.                 |
        | contruida por dos funciones:                                     |
        |         - MENU()                                                 |
        |         - OPERA()                                                |
        | Para salir del programa, escriba '0'.                            |
        |                                                                  |
        | @Athor: PAULINO BERMÚDEZ.                                        |
        | @Estudio: Becas Digitaliza Cisco. 2019-2020.                     |
        | @Su_version Python: {:2} en {:2}           |
        |         (Pulse ENTER para continuar.)                            |
        +------------------------------------------------------------------+
""".format(pythonv,sist)) 


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
    print("{:2} seleccione una de las opciones:  \n".format(username))
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
    print("13- Convertir de decimal a hexadecimal \t 14- Convertir de decimal a otra base")
    
    print(72*'_')
    print(22*"_","* Operaciones científicas.", 22*"_" )
    print(72*'_')
    print("15- Calcular el log en base 'Y' de 'X' \t 16- Calcula In de 'X'")
    print("17- Calcular el lado desconocido de un triángulo ")
    print("18- Trigonometría \t \t \t 19- Graficar una función f(x)")
    
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
        print(numero, "> ", binario(numero))
        # OPCION FÁCIL: bin(numero)
        print("Opción 2: bin()")
        print(bin(numero)[2:])

    elif (y==12):
        print("Opción: BIN a DEC")
        def decimal(binario):
            decimal=int(str(binario),2)
            return decimal

        numero = int(input('Introduce el número a convertir a decimal: '))
        print(numero, "> ", decimal(numero))
        
    elif (y==13):
        print("Opción: DEC a HEX")
        # def hexadec(decimal, base):
        #     conversion = ''                
        #     while decimal // base != 0:                
        #         conversion = str(decimal % base) + conversion                
        #         decimal = decimal // base
        #         primero = str(decimal) 
        #         segundo = conversion
        #         print(primero, "\n")
        #         print(segundo, "\n")
        #         #print(type(primero))
        #         #print(type(segundo))
        #         if primero == '10':
        #             primero = 'A'
        #         elif primero == '11':
        #             primero = 'B'
        #         elif primero == '12':
        #             primero = 'C'
        #         elif primero == '13':
        #             primero = 'D'
        #         elif primero == '14':
        #             primero = 'E'
        #         elif primero == '15':
        #             primero = 'F'
        #         if segundo == '10':
        #             segundo = 'A'
        #         elif segundo == '11':
        #             segundo = 'B'
        #         elif segundo == '12':
        #             segundo = 'C'
        #         elif segundo == '13':
        #             segundo = 'D'
        #         elif segundo == '14':
        #             segundo = 'E'
        #         elif segundo == '15':
        #             segundo = 'F'
        #         return (primero+segundo)
        numero = int(input('Introduce el número a cambiar de base: '))
        base = 16
        print(hex(numero)[2:])
        # print("Opción 2: \n", hexadec(numero, base))
        
        
    elif (y==14):
        print("Opción: DEC a base 'X'")
        def cambio_base(decimal, base):
            conversion = ''
            while decimal // base != 0:
                conversion = str(decimal % base) + conversion
                decimal = decimal // base
            return str(decimal) + conversion

        numero = int(input('Introduce el número a cambiar de base: '))
        base = int(input('Introduce la base: '))
        print(cambio_base(numero, base))
        
    elif (y==15):
        print("Opción: LOGARITMO EN CUALQUIER BASE.")
        a=float(input("Introduzca el número: "))
        b=int(input("¿Qué base? "))
        if a < 0.1:
            print("TE RECUERDO QUE: \n Los logaritmos no deben ser mayores que cero.")
        else:
            resultado=math.log(a,b)
            print("El resultado del logaritmo {:2} en base {:2} es:".format(a,b), resultado)
    
    elif (y==16):
        print("Opción: LOGARITMO NEPERIANO DE UN NÚMERO.")
        a=float(input("Introduzca el número: "))
        if a < 0.1:
            print("TE RECUERDO QUE: \n Los logaritmos no deben ser mayores que cero.")
        else:
            resultado=(a)
            print("El resultado del logaritmo neperiano de {:2} es:".format(a), resultado)
            print("ESTE DE MOMENTO NO LO HE SACADO...")
        
    elif (y==17):
        print("Opción: Lado desconocido de un triángulo.")
        tipo = input("""
            ¿Qué tipo de triángulo es? (A-D)
                a. - Equilatero
                b. - Isóceles
                c. - Escaleno
                d. - Rectángulo
        """)
        if tipo == 'a' or tipo == 'A':
            lado = int(input("Introduzca valor del lado: "))
            print("Como es un triángulo equilatero, todos sus lados son iguales, asi que")
            print("El lado desconocido es: ", lado)
        elif tipo == 'b' or tipo == 'B':
            lado2 = input("¿No sabe el lado más corto? (Y/N) ")
            if lado2 == 'y' or lado2 == 'Y':
                a=int(input("Introduzca valor del lado que conoce: "))
                interior=(2*(a**2)-(2*(a**2)*math.cos(60))
                b=(math.sqrt(interior))
                print("El lado que desconoce mide: ", b)
        
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
    