#CLASES con MEOTODS y ATRIBUTOS

# Metodo init (constructor)

class Personaje:
    #Atributos
    #En toda clase, se debe poner el inicializador o constructor
    #SIEMPRE se va a ejecutar - es lo primero -> SELF
    def __init__(self, nombre, tipo, edad): #self -> Pertenece a la misma clase donde se define
        self.nombrePersonaje = nombre    
        self.tipo = tipo
        self.edad = edad

    # Metodos especiales get y set
    def getNombrePersonaje(self):
        return self.nombrePersonaje

    def setNombrePersonaje(self, nuevoNombre: str):
        self.nombrePersonaje = nuevoNombre

    #Metodos - En metodos subinternos, lo invoco con el self.
    def saludar(self):
        print(f'Hola, soy un personaje\nMi nombre es {self.nombrePersonaje} y soy un {self.tipo}')

personaje1 = Personaje('Batman','Heroe',35)
personaje2 = Personaje('Spiderman', 'Heroe', 23)

#Fuera de los metodos, se lo invoca con punto (los invoca)
print(personaje1.nombrePersonaje)
personaje1.saludar()

print('Nombre antes del set: ',personaje1.getNombrePersonaje())
personaje2.setNombrePersonaje('Venom')
print('Nombre despuest del set: ',personaje2.getNombrePersonaje())
