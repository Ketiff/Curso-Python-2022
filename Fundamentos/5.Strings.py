#String -> str
#Es un dato indexable
#String es un tipo de dato inmutable (No acepta la rescritura o resignacion)

#Asignaciones de una unica linea
x = 'Hola'
y = ' con todos'

#String de varias lineas
texto = '''
Libro Quijote
Cervantes
En un pueblo de la mancha...
Ahi esta mi molino

print(texto)
'''
cadena1 = 'Python'
cadena2 = ' es un lenguaje de programacion'
#print(type(cadena2))

#Concatenacion de strings: es unir dos variables de tipo string en una sola impresion
#Metodo 1
numero1 =8.5
print(type(numero1))
print(cadena1, ' - ',cadena2, ' interpretado', numero1)

#Metodo 2
print(cadena1 + cadena2 + 'y ademas tengo este numero' + str(numero1))

#Metodo 3
cadena3 = cadena1 + cadena2
print(cadena3)

#POO
#Clases y Atributos
#Metodos -> funciones
#Las instancias tienen metodos

#Formated Strings
nombre = 'Kevin'
edad = 20
ira = 32.5
universidad = 'EPN'
# 1ra Forma: Basado en variables (NO tan optmimo)
print(f'1: Hola mi nombre es '+str(nombre))
# 2da Forma: Basado en variables (Optimo)
print(f'2: Hola mi nombre es {nombre} y mi edad es {edad} y tengo un ira de {ira}')
# 3ra Forma: Llama al metodo de la clase string
print('3: Hola mi nombre es {} y mi edad es {} y tengo un ira de {}'.format(nombre, edad, ira))
# 4ta Fomrma: LLama al metodo formar pero indiando la posicion
print('4: Hola mi nombre es {0} y mi edad es {1} y tengo un ira de {2}'.format(nombre,edad,ira))
# Con repeticion
print('Mi nombre es {0} studio en la {1} y ademas trabajo en {1}'.format(nombre,universidad))
# 5ta Forma: Formated string con reasignacion de variables
print('5: Hola mi nombre es {variableNombre} y mi edad es {variableEdad} y tengo un ira de {variableIRA}'
.format(variableNombre='Alexander', variableEdad=20,variableIRA=31.20))
#Objeto -> str
#Atributos -> privados
#Metodos -> format

'''
2. INDEXACION
Python
|1|2|3|4|5|
'''
cadenaTexto = 'Este es un curso de programacion'
print(cadenaTexto[0])
print(cadenaTexto[2])
# Range -> rango len
#print(len('Hola'))
# 0-> H
# 1-> o
# 2-> l
# 3-> a

print(len(cadenaTexto)) #32
print(cadenaTexto[0]) #E (izq a derecha)
print(cadenaTexto[31]) #n (izq a derecha)
#print(cadenaTexto[32]) #ERROR
#print(cadenaTexto[33]) #ERROR
print(cadenaTexto[-1]) #n (derecha a izq) 
print(cadenaTexto[-2]) #o (derecha a izq) 
print(cadenaTexto[-32]) #E (derecha a izq) 
#print(cadenaTexto[-33]) ERROR (derecha a izq) 

print(cadenaTexto[1]+cadenaTexto[8]+cadenaTexto[13]) #sur
#cadenaTexto[0]='A' Error, string no soporta la reasignacion dentro de las posiciones (es inmutable)

#Le reasigno la posicion de la cadena y en la reasignacion le coloco otro string
letra = cadenaTexto[0]
print(letra)
letra = 'A'
print(letra)

#Indexacion con RANGOS
print('-----INDEXACION CON RANGOS-----')
#RANGO: [valorIncluido:valorExcluido:Saltos]
print(cadenaTexto[0:2]) #Desde la posicion 0 hasta la posicion 1
print(cadenaTexto[0:10])
print(cadenaTexto[2:20])
print(cadenaTexto[2:20:2])#Realiza saltos de 2 en 2
# Indice hasta el final
print(cadenaTexto[2:]) #Desde el indice hasta el final
print(cadenaTexto[:3]) #Desde el comienzo hasta el indice

print(cadenaTexto[:]) #Misma salida
print(cadenaTexto[::]) #Misma salida (accedo a todo el contenido con saltos de 1)(Inicio a Fin)

#Ejericio: Invierta toda la variable cadenaTexto
print('Cadena Original: ', cadenaTexto)
print('Cadena Final: ', cadenaTexto[::-1]) #Misma salida (accedo a todo el contenido con saltos de -1) (Fin a Inicio)
 
 #Funciones en Python

print(cadenaTexto.upper()) #Se abre y cierra parentesis pq es un metodo (Todo mayusculas)
print(cadenaTexto.lower()) #Todo minusculas
print(cadenaTexto.capitalize()) #Primera mayuscula

#Encontrar algo en tu cadena de texto
print(cadenaTexto.find('curso')) #Si encuentra, devuelve el indice
print('Animales: tigre'.find('tigre')) #Si encuentra, devuelve el indice
#Si el substring no exist - me devuelve -1
print('Animales: tigre'.find('perro')) #Me devuelve el indice -1

cadenaTexto2 = 'Los niños juegan en el parque'
#Validar si empieza con...
print(cadenaTexto2.startswith('Los')) #El string que pasamos empieza con 'Los'? True
print(cadenaTexto2.startswith('Las')) #False
#Validar si termina con
print(cadenaTexto2.endswith('parque')) #El string que pasamos termina con 'parque'? True
print(cadenaTexto2.endswith('juegan')) #El string que pasamos termina con 'juegan'? False

#Funcion replace
print(cadenaTexto2.replace('juegan','se diviertien'))