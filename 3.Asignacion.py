#Asignación =


x = 5
print ('El valor de la variable x es: ', x)

#Asignación sin valor
# None = ninguno
variable1 = None
print ('Variable1', type(variable1))
print ('El valor de la variable 1 es: ', variable1)

# Inicializar una variable 'y' con el valor de 10
y = 10
print('Y = ', y)
# Multiplicar por dos
y = y * 2
print('Y = ', y)
# Multiplicar por dos
print(y*2)
print('Y = ', y)

#Asignacion con diferentes tipos
y = 'Saludo'
print('Y = ', y)

#Multiples asignaciones
#Crear las variables a y b con los valores de 2 y 3
a = 2
b = 3
a, b, c, saludo = 2, 3, 5, 'Hola'
print('A + B = ', a+b)
print(saludo)

#Asignacion del valor de una variable a otra variable
saludo2 = saludo
print(saludo2)
saludo = 'Buenas Tardes'
print(saludo)

#Ejercicio1
x1 = 4
y1 = x1 + 1
x1 = 2
print('x1 = ', x1,'y1 = ', y1)

#Ejericio2 - errores
x2,y2 = 10, 11
z2 = x2
y2 = z2 + 2
print('x2 = ',x2,'   y2 = ',y2,'  z2 = ',z2 )


