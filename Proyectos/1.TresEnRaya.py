#Tres en raya
# Reglas clásica del tres en línea
# Si tres caracteres son iguales en cualquier sentido se termina e juego
# Van a  existir dos jugadores
# Presentación del juego
# Se pueden asignar nombres a los dos jugadores
# Matriz creada a partir de listas 
# Se solicitará que se ingrese la fila y la columna en la que el jugador quiere marcar su movimiento
# Deberá comprobar si se encuentra ocupado y si si lo esta, perdera el turno
# Se terminará el juego 
# Se presente un menú al inicio en el que se pueda ingresar los nombres
# de los jugadores, y ademas escoger los caracteres, por defeco sera la x y el o
# Y la tercera opción será jugar
# Y la cuarta salir
# Ademas los resultados se guardaran en un archivo de texto con fecha, hora.
from random import randint
from weakref import finalize

#VARIABLES GLOBALES --> global
global nombreJ1 
nombreJ1 = 'Jugador 1'
global nombreJ2 
nombreJ2 = 'Jugador 2'

piezaJ1 = 'X'
piezaJ2 = 'O'

def crearMatriz():
    matriz = [] #Declaracion de matriz
    nFilas = 3
    nColumnas = 3
    for i in range(nFilas):
        matriz.append(['-']*nColumnas) #Agregar valores a la lista
        '''
    for i in range(0,nFilas):
        for j in range (0, nColumnas):
            mensaje = f'Ingrese el valor de la fila {i+1} en la columna {j+1}: '
            matriz [i][j] = int(input(mensaje))
            '''
    dimensiones = (nFilas, nColumnas)
    return matriz, dimensiones

def mostrarMatriz(matriz, dimensiones): #Argumentos que va a recibir *matriz, shape*
    filas, columnas = dimensiones
    for i in range(filas):
        for j in range (columnas):
            print(matriz[i][j], end ='\t')
        print('')    

def llenarMatriz(matriz, caracter):
    fila = int(input('Fila: '))
    columna = int(input('Columna: '))
    matriz[fila-1][columna-1] = caracter

#FUNCION def -> def NOMBREdelafuncion():
def menu():
    
    print('\n\tTres en raya\n')
    print('1. Configurar nombres jugadores')
    print('2. Cambiar piezas')
    print('3. Jugar')
    print('4. Salir')
    opcion = input('Ingrese una opcion: ')
    #print(opcion)
    return opcion #Retorna opcion de la funcion

def nombreJugadores():

    print('--- NOMBRES DE LOS JUGADORES ---')
    print('1. Cambiar el nombre del jugador 1')
    print('2. Cambiar el nombre del jugador 2')
    opcionNombre = input('Cambiar nombre del jugador: ')

    if opcionNombre == '1':
        global nombreJ1
        nombreJ1 = input('Ingrese el nombre del jugador 1: ')
    elif opcionNombre == '2':
        global nombreJ2
        nombreJ2 = input('Ingrese el nombre del jugaro 2: ')
    else: print('No ingresaste ninguna opcion valida -- ERROR --')

def cambiarPiezas():
    print('--- PIEZAS ---')
    print('1. Cambiar pieza del jugador 1')
    print('2. Cambiar pieza del jugador 2')
    opcionPieza = input('Opcion: ')
    global piezaJ1
    global piezaJ2
    if opcionPieza == '1':
        auxPieza1 = input('Pieza del jugador 1: ')
        if auxPieza1 != piezaJ2:
            global piezaJ1
            piezaJ1 = auxPieza1
        else: print('La pieza ingesada es igual a la del otro jugador')    
    elif opcionPieza == '2':
        auxPieza2 = input('Pieza del jugador 2: ')
        if auxPieza2 != piezaJ1:
            piezaJ2 = auxPieza2
        else: print('La pieza ingresada es igual a la del otro jugador')
    else: print('Ingrese una opcion valida')    

def jugar(tablero,dimensiones):
    print('--- JUGANDO ---')
    finalizado = False
    turno = randint(1,2)
    while finalizado == False:
        piezaActual = ''
        jugadorActual = ''
        if turno == 1:
            print('Es turno de: ', nombreJ1)
            piezaActual = piezaJ1
            jugadorActual = nombreJ1
            llenarMatriz(tablero, piezaJ1)
            turno = 2        
        else:
            print('Es turno de: ', nombreJ2)
            piezaActual = piezaJ2
            jugadorActual = nombreJ2
            llenarMatriz(tablero, piezaJ2)
            turno = 1    
        #Validar cuando se hizo en raya

        #Casos HORIZONTALES

        if tablero[0][0] == piezaActual and tablero[0][1] == piezaActual and tablero[0][2] == piezaActual:
            finalizado = True

        if tablero[1][0] == piezaActual and tablero[1][1] == piezaActual and tablero[1][2] == piezaActual:
            finalizado = True
        
        if tablero[2][0] == piezaActual and tablero[2][1] == piezaActual and tablero[2][2] == piezaActual:
            finalizado = True
        
        #Casos VERTICALES  
          
        if tablero[0][0] == piezaActual and tablero[1][0] == piezaActual and tablero[2][0] == piezaActual:
            finalizado = True
        if tablero[0][1] == piezaActual and tablero[1][1] == piezaActual and tablero[2][1] == piezaActual:
            finalizado = True            
        if tablero[0][2] == piezaActual and tablero[1][2] == piezaActual and tablero[2][2] == piezaActual:
            finalizado = True      
        
        #Casos Diagonales
        if tablero[0][0] == piezaActual and tablero[1][1] == piezaActual and tablero[2][2] == piezaActual:
            finalizado = True  
        if tablero[2][0] == piezaActual and tablero[1][1] == piezaActual and tablero[0][2] == piezaActual:
            finalizado = True      
        
        #En caso de que se haya llenado el tablero
        #Validar cuando se sobreescribe una posicion ocupada
        #Validar cuando todos los espacios estan llenos

        mostrarMatriz(tablero,dimensiones)
        
    print('****SE ACABO EL JUEGO****')
    print('\tEl jugador ganador es: ', jugadorActual)

def mostrarTablero():
    pass

def main():
    terminarJuego = False
    while terminarJuego == False:
        opcionMenu = menu() #Va a ejecutar la funcion menu y asigna el retorno a la variable opcion
        # Condicionales
        if opcionMenu == '1':
            nombreJugadores()
        elif opcionMenu == '2':
            cambiarPiezas()
        elif opcionMenu == '3':
            tablero, dimensiones = crearMatriz()
            jugar(tablero,dimensiones)             
        elif opcionMenu == '4':
            print('TERMINASTE EL JUEGO 🥲 ')
            terminarJuego = True
        else: print('No escogiste ninguna opcion -- ERROR --')

main() #Se ejecuta def main()...llama a la funcion menu()...y fuera de los def, ejecuto el main() principal   