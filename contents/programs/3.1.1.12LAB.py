#!/bin/python
import os
os.system("clear")
os.system("cls")


while True:    
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    income = float(input("Enter the annual income: "))
    print("vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv \n")
    base = 85528
    #
    # Calculating tax. 
    #
    if income == -0:
        print("Finished program")
        break
    elif income < base or income == base:
        print("Calculamos el 18% de los ingresos")
        tax = income*.18
        print("El 18% de sus {:.02f} (ingresos) es {:.02f} (Pre-Tazas) ".format(income,tax))
        
        print("Restamos los 556.02 de DF")
        tax -= 556.02
        tax = round(tax, 0)
        
        if tax < 0:
            tax = 0.0
            print("The tax is: {:.02%} thalers".format(tax))
        print("----------------------------------------------------------")
        print("The tax is: ", tax, "thalers")
        print("----------------------------------------------------------")

    elif income > base:
        # Excedente
        surplus=(income-base)
        print("Aplicamos el 32% sobre el excedente: ", surplus)
        surplus *=.32
        print("El 32% del extra es: ", surplus)
        tax = surplus
        print("Pre-Tazas: ", tax)
        
        # print("La pre-taza {:.02f} con los DF de sus impuestos es: 14839.02".format(tax) )
        tax += 14839.02
        print("----------------------------------------------------------")
        tax = round(tax, 0)
        print("The tax is: ", tax, "thalers")
        print("----------------------------------------------------------")
    else:
        print("Error in the income input")
