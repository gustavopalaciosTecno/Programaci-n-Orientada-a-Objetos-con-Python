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


nombre1 = input("Coloca tu nombre acá: ")
edad1 = int(input("Coloca tu edad acá: "))		

persona = Persona(nombre1,edad1)
print(persona)


nombre2 = input("Coloca tu nombre acá: ")
edad2 = int(input("Coloca tu edad acá: "))
sueldo = float(input("Coloca tu sueldo acá: "))

empleado = Empleado(nombre2,edad2,sueldo)
print(empleado)			

# Cambiar los datos
empleado.nombre = "Lautaro"
empleado.edad = 46
empleado.sueldo = 180000.10
print(empleado)	







