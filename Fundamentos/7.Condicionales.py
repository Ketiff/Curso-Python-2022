# SI, SINO, ENTONCES
# IF, ELSE, IF ELSE

from cgitb import text


variable1 = True
variable2 = False
'''
#Operador
print(1 == 1) #True
print('Hola' == 'Hola') #True
print('hola' == 'Hola') #False
'''
if variable1 and variable2 == True: print('La expresion es verdadera') # Bloques de codigo despues de :
else: 
    print('La expresion es falsa')

#Comprobaciones

texto = 'Kevin'
#En python se puede omitir la comparacion a verdadero
#if texto.startswith('K') == True: 
#Es igual a escribir
if texto.startswith('K'):
    pass #Le digo a python que no quiero hacer nada y valida la condicion 

if texto.startswith('K'):
    print ('Tu nombre empieza con K')
elif texto.startswith('B'): #elif = else if
    print('Tu nombre empiza con la B')    
else:
    print('Tu nombre no empieza con K ni B')

# Otro tipo de comparaciones
print(10>20) # False
print(10>=10) #True
print(20<30) #True 
print(500 != 200) #True
print(200 != 200) #False
print('Kevin' != 'Alexander') #True
x = 10
print(0 < x < 12) #True
print(4 < 5 < 8 < 200) #True
print('A' > 'B') #False - Se lo toma alfabeticamente
print('oso' < 'osa') #False - verifica de manera secuencial cual letra es mayor en el diccionario

