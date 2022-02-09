'''
Palindromos:
Soliciar al usuario que ingrese por teclado un texto, luego, le vamos a indicar
si lo ingresado es o no un palindromo.
'''

texto = str(input('Ingrese una cadena de texto: '))
print('\nPalabra de izq a derecha: '+texto)
print('Palabra de derecha a iza: '+texto[::-1]+'\n')
if texto == texto[::-1]:
    print('Ingresaste un palindormo')
elif texto.lower() == texto[::-1].lower():
    print ('Palindromo ignorando las mayusculas')
elif texto.replace(' ','') == texto[::-1].replace(' ',''):
    print('Palindromo ignorando los espacios')
elif texto.lower().replace(' ', '') == texto[::-1].lower().replace(' ', ''):
    print('Palindromo ignorando las mayusculas y espacio')    
else:
    print('No ingresaste un palindromo')    