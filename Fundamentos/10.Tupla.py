#Tupla -> tuple
#Inmutable: Una vez inicializada, no se podra modificar - Para dimensiones fijas - Interefaces
#- Valores NO alterados

tupla1 = (3,4,6,6) #inicializacion

print(tupla1)
print(type(tupla1))

#Accediendo a los elementos de la tupla
print(tupla1[0])

# tupla1[0] = 8 - ERROR

#Tupla cn diferentes tipos de datos
tupla2 = (True,25,'Hola')
print(tupla2)

#Averiguar si un elemento se encuentra o no en una lista
print(False in tupla2) #Averiguar si False esta en tupla 2
print('Python' in tupla2) #Averiguar si Python esta en la tupla 2
print(25 in tupla2) #Averiguar si 25 esta en la tupla 2
print(100 not in tupla2) #Averiguar si 100 no esta en la tupla 2

#Metodo de la tupla 
print(tupla1.index(3)) #Posicion
# print(tupla1.index(100)) en caso de no estar incluido devuelve error
print('Tamaño de una tupla', len(tupla1))
print('Cuantos # 6 estan en la tupla 1? ')
print('> ',tupla1.count(6))

#DIMENSIONES
dimensiones = (500,600)
dimensionX, dimensionY = dimensiones
print(dimensionX)
print(dimensionY)
print(dimensiones)

#Convertir de una lista hacia tupla
lista1 = [85, 26, 98]
