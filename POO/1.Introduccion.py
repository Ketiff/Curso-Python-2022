# POO
# Prototipo - Plantilla

# CLASE
#-> Atributos(caracteristicas)
#-> Metodos
# ADT = Abstract Data Type

class Curso:
    pass

class Alumno:
    pass
#Instanciar una clase -> Objeto

curso1 = Curso()
curso2 = Curso()
print(type(curso1))

cursos = [curso1, curso2]
print(cursos)

texto = 'Hola'
print(texto.capitalize())

# POO en python
# Saber de quien esta instanciado un objeto
print('Comprobar si curso 1 es instancia de Curso: ', isinstance(curso1,Curso))
print('Comprobar si curso 1 es instancia de Alumno: ', isinstance(curso1,Curso))
