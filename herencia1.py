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

# class Colaborador:
# 	def __init__(self,dni.nombre,apellido,edad,salario):
# 		self.__dni = self.validar_dni(dni)
# 		self.__nombre = nombre
# 		self.__apellido = apellido
# 		self.__edad = edad
# 		self.__salario = self.validar_salario(salario)

# 	@property
# 	def dni(self):
# 		return self.__dni


# 	@property
# 	def nombre(self):
# 		return self.__nombre.capitalize()

# 	@property
# 	def apellido(self):
# 		return self.__apellido.capitalize()	


# 	@property
# 	def edad(self):
# 		return self.__edad

# 	@propery
# 	def salario(self):
# 		return self__salario	
				
# 	@salario.setter
# 	def salario(self,nuevo_salario):
# 		self__salario = self.validar_salario(nuevo_salario)

 	
#  	def validar_salario(self,salario):
#  		try:
#  			salario_num = float(salario)
#  			if salario_num < 0:
#  				raise ValueError("El salario debe ser un número positivo")
#  			return salario_num	
# 		except Exception as e:
#  			raise ValueError("El salario debe ser un número válido")
 	
#  	def validar_dni(self,dni):
#  		try:
#  			dni_num = int(dni)	
#  			if len(str(dni)) not in [7,8]:
#  				raise ValueError("El DNI debe tener 7 u 8 dígitos")
# 			if dni_num <= 0:
# 				raise ValueError("El DNI debe ser un número positivo") 				
#  		except ValueError:
#  			raise ValueError("El dni debe ser numérico y estar compuesto por 7 u 8 dígitos")
 		 		

# 	def to_dict(self):
# 		return {
# 			"dni":self.dni,
# 			"nombre":self.nombre,
# 			"apellido":self.apellido,
# 			"edad":self.edad,
# 			"salario":self.salario
# 		}	

# 	def __str__(self):
# 		return f"{self.nombre} {self.apellido}"

# class ColaboradorTiempoCompleto(Colaborador):
# 	def __init__(self,dni,nombre,apellido,edad,salario,departamento):
# 	super().__init__(dni,nombre,apellido,edad,salario)
# 	self.__departamento = departamento

# 	@property
# 	def departamento(self):
# 		return self.__departamento	

# 	def to_dict(self):
# 		data = super().to_dict()
# 		data['departamento'] = self.departamento
# 		return data

# 	def __str__(self):
# 		return f'{super().__str__()} - Departamento: {self.departamento}'			








