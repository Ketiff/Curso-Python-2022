# NUMEROS ENTEROS -> int
# Conversiones de datos

#Importaciones de librerias
import math as math

'''
#La funcion input transforma todo a string
num1 = input('Ingresa un numero: ') #num1 es tipo str
print(type(num1))
num1 = int(num1, 2) #Lo convierte a base binaria
print(type(num1))
print(num1)

#Conersion en una sola linea e impresion
num2 = int(input('Ingrese otro numero: '))
print(num2+2)


ERROR
num3 = int('pooo')
print(num3)



num3 = int(True)
# True -> 1
# False -> 0
print(num3)
'''

#Operadores numericos (Suma, Resta, Multi, Divi)
a,b = 2,3
print('\n\tOperaciones con numeros')
print('Suma: ', a+b)
print('Resta: ', a-b)
print('Multiplicacion: ', a*b)
#print('Division: ', a/b)
#La division de dos numeros siempre sera un numero flotante
#Conversion: print(int(10/3))

#Potencia
print('Potencia: ', 2**3)

#Modulo
print('Modulo: ',b%a)

#Division entera
print('Division entera', 10//3)

#Raiz - Su resultado es flotante
print('Raiz con potencia: ', 64**(1/2))
print('Raiz: ', int(math.sqrt(64)))

#