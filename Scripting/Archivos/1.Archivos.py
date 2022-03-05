# Manejo de Archivos
# Windows -> abrir texto y binario
# Linux y MacOS: -> Se abre de unica forma
 
#Modos de tomar un archivo
# w (write) -> wt (modo texto) y wb (modo binario) y w+ (Dame el permiso siguiente)
# r (read) -> rt (modo texto) y rb (modo binario) y r+  (Dame el permiso siguiente)
# a () -> at (modo texto) y ab (modo binario)
# 

# archivo = open('direccion y el archivo.txt', 'Modo de tomar archivo')


miArchivo = open('Scripting/Archivos/ejemplo.txt', 'r') #Estoy en la direccion hasta Curso-Python-2020
#Debo añadirle la dirección faltante (Se especifica la carpeta)
print(type(miArchivo))
print(miArchivo)

#Como leer un archivo
print(miArchivo.read())
print('---Despues---')
miArchivo.seek(0) #Permitir redireccionar al puntero a (0)
print(miArchivo.read())

#Leer varias lineas
print('---Leer variable linea---')
miArchivo.seek(0)
print(miArchivo.readlines())




