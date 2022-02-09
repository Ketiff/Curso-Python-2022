#Usuario ingresa un numero y le diremos si es par o impar

from distutils.command.install_scripts import install_scripts


numero = int(input('Ingresa un numero: '))
if numero%2 == 0:
    print('Es un numero par')
else:
    print('Es un numero impar') 

if numero>0:
    print('Es un numero mayor a 0')
else:
    print('Es un numero menor a 0')    