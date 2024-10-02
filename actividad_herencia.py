"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, 
las cuales heredan de la clase Padre Vehiculo

Instrucciones de tareas

Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, 
las cuales heredan de la clase Padre Vehiculo.

La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):

-Atributos (color, ruedas)

-Métodos ( __init__() y __str__ )

Coche (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):

-Atributos ( velocidad (km/hr) )

-Métodos ( __init__() y __str__() )

Bicicleta (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):

-Atributos ( tipo (urbana/montaña/etc )

-Métodos ( __init__() y __str__() )
"""
### clase vehículos
class Vehiculo:
	def __init__(self,nombre,color,ruedas):
		self.color = color
		self.ruedas = ruedas
		self.nombre = nombre
	def __str__(self):
		return "Nombre:" + self.nombre + "\nColor: " + self.color + "\nCantidad de ruedas:" + str(self.ruedas)	


class Coche(Vehiculo):
	def __init__(self,nombre,color,ruedas,velocidad):
		super().__init__(nombre,color,ruedas)
		self.velocidad = velocidad

	def __str__(self):
		return super().__str__() + "\nVelocidad: " + self.velocidad

class Bicicleta(Vehiculo):
	def __init__(self,nombre,color,ruedas,tipo):
		super().__init__(nombre,color,ruedas)
		self.tipo = tipo

	def __str__(self):
		return super().__str__() + "\nTipo: " + self.tipo

class Triciclo(Vehiculo):
	def __init__(self,nombre,color,ruedas,tipo):
		super().__init__(nombre,color,ruedas)
		self.tipo = tipo

	def __str__(self):
		return super().__str__() + "\nTipo:" + self.tipo			

cochePadre = Vehiculo("Vehiculo automotor","Rojo",4)		
print(cochePadre)
cocheHijo = Coche("Cuatriciclo","Verde",4,"45km/h")
print(cocheHijo)
biciHija = Bicicleta("Bicicleta","Azul",2,"Mountain Bike")
print(biciHija)
tri = Triciclo("Triciclo","verde agua",3,"Para niños")
print(tri)

