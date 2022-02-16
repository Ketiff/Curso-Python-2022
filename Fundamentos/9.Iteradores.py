# Iteraciones
#for es una isntrucción que permite recorreer un iterable

listaFrutas = ['Pera','Manzana','Banano']

for fruta in listaFrutas: # for NOMBRE in LISTA
    print(fruta) #Trabajo con el NOMBRE

# Utilizar rangos numéricos
for item in range(0,5): #Recibe un rango (INICIAL,FINAL) Inicial = incluido ; Final = excluido
    print('Elemento {}'.format(item))

matriz = [
    [0,1,0],
    [1,1,1],
    [0,0,2]
]

# Anidados
for fila in matriz:
    for columna in matriz:
        print(fila)
        print(columna)

# Anidados basados en índices
for i in range(len(matriz)):
    for j in range(len(matriz[i])):  
        print('valor de la posición i:{} - j:{} es:{}'.format(i,j,matriz[i][j]))
        if matriz[i][j] == 2:
            matriz[i][j] = 10

print(matriz)
        
# While
