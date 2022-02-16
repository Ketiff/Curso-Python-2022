#-------BOLEANOS------- 
#bool()
# ---Parte 1: Bolean
# Dos tipos (True/False)
#True = 1 / False = 0

from ast import And, Not
from operator import truediv
from pickle import FALSE
from traceback import print_tb


variable1 = True
variable2 = False

print(type(variable1))
print(variable1.bit_length()) #Transformo a bits

# ---Parte 2: Operadores
# Asignacion =
# Aritmeticos
# Strings + -> Concatenacion

# Asignacion Complementarios---
x = 4
x += 5 #Le sumo 5 a x
print(x)
x *= 2 #Le multiplico 2 a x
print(x)

x **= 3 #Le elevo al cubo
print(x)

# Operadiores Logicos---
# Conjuncion (y) -> and
print(variable1 and variable2)
print(True and True)
print(False and False)

# Disyuncion (o) -> or
print(variable1 or variable2)
print(True or True)
print(False or False)

# Negacion -> not
print(not variable1)
print(not variable2)

# Operadores bit a bit ^ (Compara bit a bit)

print ('1: ',4 ^ 5) #1 - Convierte  binario y luego realiza la operacion - 1 ^ 1
print ('2: ',True and True) # True - Operacon logica de toda la expresion - True and True
print('3: ',True & True) # True - Tomar el truly or falsy y hacer la operacion and
# AND
print(True & True)

# OR
print(4 | False)

# XOR
print(4 ^ 5)

# NOT
print(~False)

# Desplazamiento de bit a bit hacia la derecha
print(True >> False)
# Desplazamieto bit a bit hacia la izq
print(True << False)

# Operadores Bit a bit
# Base 10 -> 0,1,2,3,4,5,6,7,8,9
# Binario -> 0,1
# 1 Byte -> 8 bits

# 10101010 -> 1 byte
# 2^{7},...,2^{1}, 2{0}
#           16,4,2,1
# Computadora representame el numero 3 en un byte (8 bits) 
# 00000011 (base 10)
# Computadora representame el numero 5 en un byte (8 bits)
# 5 (base 10) 4 + 1 = 5
# 00000101 = 5


#Ejemplo de los operadores bit a bit
var1 = 2 # 00000010 -> 10
var2 = 3 # 00000011 -> 11
var3 = 5 # 00000101 -> 101

print('---PROBANDO LOS BINARIOS---')
print('variable 1: ', var1)
print('variable 2: ', var2)
print(var1 & var2)
# var1 ->  1 0
# var2 ->& 1 1
#      --------
#          1 0  -> 2 (base 10)
print(var1 | var2)
# var1 ->  1 0
# var2 ->| 1 1
#      --------
#          1 1  -> 3 (base 10)
print(var1 ^ var2)
# var1 ->  1 0
# var2 ->^ 1 1
#      --------
#          0 1  -> 1 (base 10)
print(~var1)
# var1 -> 00000010
#         ~
#         11111101
print(var1>>var2)
#  10
#  11
#   0


# Operadores de Pertenencia
