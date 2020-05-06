#!/bin/python 
import os, sys, getpass, platform
import math, time
import matplotlib.pyplot as plt
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
        |         - MAIN()                                                 |
        |         - OPERA()                                                |
        | Para salir del programa, escriba '0'.                            |
        |                                                                  |
        | @Athor: PAULINO BERMÚDEZ.                                        |
        | @Estudio: Becas Digitaliza Cisco. 2019-2020.                     |
        | @Su_version Python: {:2} en {:2}           |
        |         (Pulse ENTER para continuar.)                            |
        +------------------------------------------------------------------+
    """.format(pythonv,sist)) 

def main():
    os.system('clear')
    os.system('cls')
    
    # time.sleep(1)
    # Menú
    username = getpass.getuser()
    print(72*'_')
    print(27*'_',' CALCULADORA ',30*'_')
    print(72*'_')
    print(33*' ','|')
    print(72*'_')
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
    print("18- Trigonometría \t \t \t 19- Graficar una función f(x)**")

    print("\n\n** PTE de revisar")
    
    print()
    print("0 -  SALIR. ")
    y = int(input("Opción: "))
    print()
    opera(y)
    time.sleep(3)
    while True:
        try:
            main()
        except ValueError:
            pausa=input("ALGO SALIO MAL...F...MAAAALLL!!! --- ENTER para volver al menú.")
            main()

def opera(y):
    # En caso de ENTER sin número...    
    print("__________________")    
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
        print("Genial, ha seleccionado: ", tipo)
        print()
        if tipo == 'a' or tipo == 'A':
            lado = int(input("Introduzca valor del lado: "))
            print("Como es un triángulo equilatero, todos sus lados son iguales, asi que")
            print("El lado desconocido es: ", lado)
        elif tipo == 'b' or tipo == 'B':
            lado2 = input("¿Es el lado desigual? (Y/N) ")
            if lado2 == 'y' or lado2 == 'Y':
                a=int(input("Introduzca valor del lado que conoce: "))
                interior=(2*(a**2)-(2*(a**2)*math.cos(60)))
                b=(math.sqrt(interior))
                print("El lado que desconoce mide: ", b)
            else:
                print("Como es isóceles, dos de sus lados son iguales.")
                print("Lado desconocido: ", a)
        elif tipo == 'c' or tipo == 'C':
            print("""
                       
                A
                *
                | + +
                |  +    +
                |   +     +    
            h   |     +     +   c
                |      +       +        
                |     b +        +          
                |        +          +    
                |         +           +      
                |          +              +    
            -+-        C *---------------* B
                               a
            """)
            h = input("¿Sabes la altura (h)? (Y/N) ")
            if  h=='N' or h=='n':
                print("Genial!")
                lado=input("¿Qué lado desconocemos? (a/b/c)")
                lado=lado.upper
                if lado == 'A' :
                    ang=float(input("¿Ángulo de 'A'? "))
                    b = float(input("Lado 'b': "))
                    c = float(input("Lado 'c': "))
                    a = ((b**2)+(c**2)-(2*b*c*math.cos(ang)))
                    print()
                    print("""Tenemos:
                    - a: {:2}
                    - b: {:2}
                    - c: {:2}
                    """.format(a,b,c))
                elif lado == 'B':
                    ang=float(input("¿Ángulo de 'B'? "))
                    a = float(input("Lado 'a': "))
                    c = float(input("Lado 'c': "))
                    b = ((a**2)+(c**2)-(2*a*c*math.cos(ang)))
                    print()
                    print("""Tenemos:
                    - a: {:2}
                    - b: {:2}
                    - c: {:2}
                    """.format(a,b,c))
                elif lado == 'C':
                    ang=float(input("¿Ángulo de 'C'? "))
                    a = float(input("Lado 'a': "))
                    b = float(input("Lado 'b': "))
                    c = ((b**2)+(a**2)-(2*b*a*math.cos(ang)))
                    print()
                    print("""Tenemos:
                    - a: {:2}
                    - b: {:2}
                    - c: {:2}
                    """.format(a,b,c))
                else:
                    print("Error en los datos de entrada")
            else:
                h=input("Dime la altura")
                lado=input("¿Qué lado calculamos? (A-C) ")
                lado = lado.upper
                if lado == 'A':
                    ang = float(input(" ¿Ángulo de 'B'? "))
                    a = h/(math.sin(ang))
                    print("El lado 'a' mide: ", a)
                elif lado == 'B':
                    ang = float(input(" ¿Ángulo de 'A'? "))
                    b = h/(math.sin(ang))
                    print("El lado 'a' mide: ", b)
                elif lado == 'C':
                    a = float(input("Valor de 'a': "))
                    b = float(input("Valor de 'b': "))
                    if h < b:
                        hipo = h**2
                        cat2 = b**2
                    else:
                        hipo = b**2
                        cat2 = h**2
                    x = (math.sqrt(hipo-cat2))
                    base = x + a 
                    c = math.sqrt((base**2)+(h**2))
                    print("El lado 'c' mide: ", c)
                else:
                    print("Error en los datos de entrada")
        elif tipo == 'd' or tipo == 'D':
            lado = input("¿Qué lado desconoce? (c1 , c2 o h) ")
            if lado == 'c1' or lado == 'C1':
                h =input("Hipotenusa: ")
                c2 =input("Cateto :") 
                c1 = math.sqrt((h**2)-(c2**2))
                print(" La medida del cateto es: ", c1)
            elif lado == 'c2' or lado == 'C2':
                h =input("Hipotenusa: ")
                c1 =input("Cateto :") 
                c2 = math.sqrt((h**2)-(c1**2))
                print(" La medida del cateto es: ", c2)
            elif lado == 'h' or lado == 'H':
                c1 =input("Cateto 1: ")
                c2 =input("Cateto 2:") 
                h = math.sqrt((c1**2)+(c2**2))
                print(" La medida de la hipotenusa es: ", h)                
    elif (y==18):
        print("Opción:Trigonometría")
        ang = float(input("¿Ángulo? "))
        print("")
        print("""
        OPCIONES (Sin usar pitágoras):
        Calcula
            1- La tangente de un ángulo. 
            2- El seno de un ángulo.
            3- El coseno de un ángulo.
            4- La cotangente de un ángulo
        """)
        opcion =int(input("Seleccione una opcion: "))
        
        c1 = math.tan(ang)
        c2 = math.sin(ang)
        c3 = math.cos(ang)
        c4 = math.tanh(ang)

        # Diccionario de minioperaciones
        opciones = {1:c1,2:c2,3:c3,4:c4}
        
        print(15*"_____")
        print(opciones)
        print(15*"_____")
        
        valor = opciones.get(opcion)
        clave = list(opciones.keys())[list(opciones.values()).index(valor)]

        print("Resultado en RADIANES de la opción ", clave , " es: ", valor)
    
        # Recuerda que la fórmula de calcularlo manualmente es:
        # 
        # - tan x = sen x / cos x    ;  tan x = 1 / cotang x ; (Por pitágoras) sen^2(x)+cos^2(x)=1
        # - sen x = 1 / cos x
        # - cos x = 1 / sen x
        # - cotan x = cos x / sen x  ;  1 + tang^2(x) = sec^2(x) 
        # - tan x = 1 / cot(x)  
    #elif (y==19):
        # print("Opción: Gráficas de una función")
        # import pandas as pd
        # import numpy as np

        # pausa = input("""
        
        #         Hola de nuevo!
        #         Nada, quería comentarte que en esta parte del programa
        #         soy un poco más FAIL aunque ando aprendiendo para mejorar mi agilidad
        #         en este tipo de problemas...
                
        #         Te comento, resuelvo gráficas simples:
        #             - 1er grado.
        #             - 2do gradp.
        #             - 3er grado.
        #             - Raices.
        #             - Logaritmicas.
        #         Aun así, lo intentaré hacer lo mejor posible.

        #         Vamos allá!
                
        #         [ Cuándo estés listo, pulsa ENTER para continuar. ]
        # """)        

        # def f(x):
        #     os.system('clear')
        #     os.system('cls')
        #     print(""" TIPOS.
        #             1- 1er grado.
        #             2- 2do gradp.
        #             3- 3er grado.
        #             4- Raices.
        #             5- Logaritmicas.
        #     """)
        #     tipo = int(input("¿Tipo de función? 1-5. :"))
        #     funcion = input ("Escriba la función: ")
        #     funcion = funcion.lower()
        #     print("Su función es: ",funcion)
        #     if tipo == 5:
        #         return np.log(funcion)
        #     elif tipo == 4:
        #         return np.sqrt(funcion)
        #     elif tipo == 3:
        #         return np.power(funcion,3)
        #     elif tipo == 2:
        #         return funcion
        #     elif tipo == 1:
        #         return funcion
        #     else:
        #         print("He tenido un problema resolviendo la función.")
 
        # x = np.array([4, 8, 0, 6, 2, -2]) #Crear vector valores de x

        # y = f(x)
        # n = input("PARADA 484")

        # #Tabla de los valores de la funcion
        # tabla = pd.DataFrame(list(zip(x, y)), columns=['x', 'f(x)'])
        # print(tabla)
        # n = input("PARADA 489")
        # def move_spines():
        #     # Esta funcion divide pone al eje 'Y' en el valor 0 de 'X para dividir claramente los valores positivos y negativos.
        #     fix, ax = plt.subplots()
        #     for spine in ["left", "bottom"]:
        #         ax.spines[spine].set_position("zero")
            
        #     for spine in ["right", "top"]:
        #         ax.spines[spine].set_color("none")
            
        #     return ax
        # n = input("PARADA 500")
        # x = np.linspace(-2, 6, num=30)

        # ax = move_spines()
        # ax.grid()
        # ax.plot(x, f(x))
        # plt.title(r"Grafico.")
        # plt.ylabel('f(x)')
        # plt.xlabel('x')
        # plt.show() 
        # n = input("PARADA 510")    
# Programa principal
if __name__ == "__main__":
    main()