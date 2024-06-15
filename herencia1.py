class Persona:
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad

	def __str__(self):
		return "Nombre: " + self.nombre + " Edad: " + str(self.edad)	



class Empleado(Persona):
	def __init__(self,nombre,edad,sueldo):
		super().__init__(nombre,edad)
		self.sueldo = sueldo

	def __str__(self):
		return super().__str__() + " Sueldo:" + str(self.sueldo)

persona = Persona("Alberto",55)
print(persona)

empleado = Empleado("Lidia",48,480000)
print(empleado)			

# Cambiar los datos
empleado.nombre = "Lautaro"
empleado.edad = 46
empleado.sueldo = 180000.10
print(empleado)	





