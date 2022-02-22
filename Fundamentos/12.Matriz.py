#  Una funcion generica que permita crear una matriz
#LLENAR LA MATRIZ
from tkinter.tix import COLUMN
from xml.dom.xmlbuilder import DOMImplementationLS


def crearMatriz():
    matriz = [] #Declaracion de matriz
    nFilas = int(input('Ingrese el numero de filas: '))
    nColumnas = int(input('Ingrese el numero de columnas: '))
    for i in range(nFilas):
        matriz.append([0]*nColumnas) #Agregar valores a la lista
    for i in range(0,nFilas):
        for j in range (0, nColumnas):
            mensaje = f'Ingrese el valor de la fila {i+1} en la columna {j+1}: '
            matriz [i][j] = int(input(mensaje))
    dimensiones = (nFilas, nColumnas)
    return matriz, dimensiones


#Funcion generica para imprimir en consola cualquier matriz (con argumento)
def mostrarMatriz(matriz, dimensiones): #Argumentos que va a recibir *matriz, shape*
    filas, columnas = dimensiones
    for i in range(filas):
        for j in range (columnas):
            print(matriz[i][j], end ='\t')
        print('')    

def llenarMatriz(matriz, fila, columna):
    matriz[fila-1][columna-1] = 'X'


def main():
    matriz,dimensiones = crearMatriz()
    mostrarMatriz(matriz, dimensiones)
    llenarMatriz(matriz,2,2)
    print('')
    mostrarMatriz(matriz, dimensiones)
main()    