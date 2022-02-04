''' Programa que permita resolver una ecuacion de segundo grado
ax^(2)+bx+c=0 -> a, b y c son numeros enteros
Pedir al usuario que ingrese los valores de a, b y c
Imprimiremos en consola el polinomio y las dos soluciones
'''
import math as math
print('Forma de la ecuacion: ax^(2)+bx+c = 0')

a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c: '))

r1 = (-b + math.sqrt((b**2)-(4*a*c)))/ (2*a)
r2 = (-b - math.sqrt((b**2)-(4*a*c)))/ (2*a) 

print ('El polinomio es: ',a,'x^(2) +',b,'x +',c)
print ('Solucion 1: ', r1)
print ('Solucion 2: ', r2)

