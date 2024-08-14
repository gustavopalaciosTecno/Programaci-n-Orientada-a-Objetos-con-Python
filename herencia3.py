class Gerente:
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad

	def __str__(self):
		return f"Nombre: {self.nombre} - edad: {self.edad}"

class Empleado(Gerente):
	def __init__(self,nombre,edad,sueldo):
		super().__init__(nombre,edad)
		self.sueldo = sueldo

	def __str__(self):
		return super().__str__() +  " sueldo " +  str(self.sueldo)			

emp1 = Gerente("Ismael", 55)
emp2 = Empleado("Ricarda",78,1250000)
print(emp1)			
print(emp2)