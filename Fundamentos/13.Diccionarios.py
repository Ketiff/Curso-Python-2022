'''
Diccionarios
Hash maps
Tiene dos partes: clave (llave) y el valor
Tras la inicializacion, la clave es inmutable

Plabra reservada: dict
diccionario1 = {}
'''



diccionario1 = {
    'i1': 1,
    'i2': [True,'Kevin', 6]
}

print(diccionario1)
print(type(diccionario1))

#Acceder a los datos de un diccionario
print(diccionario1['i2'])

#------------------------------------------------

materias = {
    'Fundamentos de redes' : 10,
    'Probabilidad' : 12
}

edad = 21
llaveVariable = 'cedula'
persona = {
    'nombre': 'Kevin',
    'apellido': 'Revelo',
    'edad': edad,
    'casado': False,
     2: 'Dos',
     llaveVariable : '1727570648',
     'materias' : materias
}

print(persona['nombre'])
print(type(persona['edad']))
print(persona['casado'])
print(persona[2])
print(persona[llaveVariable])
print(persona['materias'])

listaPrueba = [0,1,2,3,4]

print('-----------Metodos---------')

#Obtener un valor con metodo
print(persona.get('edad'))

#Actualizar un dato
persona.update({'edad' : 23})
print(persona.get('edad'))

#Agregar un valor a un diccionario ya creado
persona['Universidad'] = 'EPN'
print(persona)

#Eliminar valores de un diccionario

#pop eliminacion a traves de la llave
persona.pop(2)
print(persona)

# 1. Saber los valores del diccionario
# for value in persona.values()
print(persona.values())

# 2. Sabre los valores de las llaves
# for llave in persona.keys()
print(persona.keys())

#3. Diccionario mapeado
print(persona.items())
#Encontrar una llave dado un valor
for llave, valor in persona.items():
    if '1727570648' == valor:
        print(llave)
    #print(f'llave: {llave} valor: {valor}')

#Funciones para encontrar una llave dado un valor
def obtenerLlave(valorBuscar):
    for llave, valor in persona.items():
        if valorBuscar == valor:
            return llave

print('Llave correspondiente encontrado: ', obtenerLlave('1727570648'))
persona.pop(obtenerLlave('1727570648'))
print(persona)

# Pop item -> Elimina el ultimo valor del diccionario
persona.popitem()
print(persona)

#Que pasaria si pido obtener un valor?
print(persona.get('mascota', 'No existe este valor'))

copiaPersona = persona.copy()
print(copiaPersona)

#Numerable
print(len(copiaPersona))

#Eliminar todo
copiaPersona.clear()
print(copiaPersona)

#Conversion lista a diccionario

# 1
listaPrueba = [0,1,2,3,4,]
diccionarioPrueba = {}
for i in listaPrueba:
    diccionarioPrueba[i] = i
print(diccionarioPrueba)

# 2
diccionarioPrueba2 = {}
listaLlave = ['n0','n1','n2','n3','n4']
listaPrueba2 = [0,1,2,3,4]
for i in range(len(listaLlave)):
    diccionarioPrueba2[listaLlave[i]] = listaPrueba2[i]
print(diccionarioPrueba2)

# 3
diccionarioPrueba3 = dict(zip(listaLlave,listaPrueba2))
print(diccionarioPrueba3)