blocks = int(input("Enter the number of blocks: "))

# Tengo la siguiente situación:
# Para tener: 
#  1) altura          2) alturas          3) alturas            4) alturas          5) alturas
# Necesito que:
#                       *                       *                    *                      *       | 1
#  *                   * *                     * *                  * *                    * *      | 2
#                                             * * *                * * *                  * * *     | 3
#                                                                 * * * *                * * * *    | 4
#                                                                                       * * * * *   | 5
# Los saltos son proporcionales porque son sumando 1 unidad.
#           +2                  +3                      +4                      +5
# Para saber qué número de bloques necesita cada altura es aplicando:
#
#  bloques = (h * (h + 1)) / 2
#
# Como el problema a resolver es el contrario, aplico la inversa de la operación:
#
# bloques * 2 = h ( h + 1) ==> Altura (H)
# H => ((2*bloques) -h^2-h) = 0
# H => h^2+h-(2*bloques)=0
#
# Descartamos los valores negativos de la operación cuadrática y tenemos la altura.

# Inicializamos con la altura mínima que es 1 
h=1
eq=(h^2 + h - (2*blocks))

print("The height of the pyramid: "+ eq)
while eq >= 0:
    print("Vuelta nº:" + blocks )
    blocks -= 1
    eq -= 1



print("The height of the pyramid:", height)