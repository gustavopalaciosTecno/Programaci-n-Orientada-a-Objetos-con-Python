# Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, 
# las cuales heredan de la clase Padre Vehiculo
# Instrucciones de tareas
# Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta, 
# las cuales heredan de la clase Padre Vehiculo.
# La clase padre debe tener los siguientes atributos y métodos
# Vehiculo (Clase Padre):
# -Atributos (color, ruedas)
# -Métodos ( __init__() y __str__ )
# Coche (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
# -Atributos ( velocidad (km/hr) )
# -Métodos ( __init__() y __str__() )
# Bicicleta (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
# -Atributos ( tipo (urbana/montaña/etc )
# -Métodos ( __init__() y __str__() )

class Vehiculo:
	def __init__(self,color,ruedas):
		self.color = color
		self.ruedas = ruedas

	def __str__(self):
		return f"Color: {self.color} - Cantidad de ruedas: {self.ruedas}" 	


class Coche(Vehiculo):
	def __init__(self,color,ruedas,velocidad):
		super().__init__(color,ruedas)
		self.velocidad = velocidad

	def __str__(self):
		return super().__str__() + " Velocidad:  " + str(self.velocidad) + " km/h"		

class Bicicleta(Coche):
	def __init__(self,color,ruedas,velocidad,tipo):
		super().__init__(color,ruedas,velocidad)
		self.tipo = tipo

	def __str__(self):
		return super().__str__() + " Tipo: " + self.tipo


coche1 = Vehiculo("rojo",4)	
print(coche1)	
coche2 = Coche("verde",2,"150")
print(coche2)
coche3 = Bicicleta("azul",2,85,"urbana")
print(coche3)
coche4 = Bicicleta("plateada",2,90,"montaña")
print(coche4)		




