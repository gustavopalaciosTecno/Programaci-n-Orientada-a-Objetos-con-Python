class Persona:
	def __init__(self,nombre,apellidoPaterno,apellidoMaterno):
		self.nombre = nombre
		self._apeP = apellidoPaterno
		self.__apeM = apellidoMaterno

	def metodoPublico(self): # Para acceder al método privado, es importante accederlo desde un método público
		self.__metodoPrivado()	


	def _metodoProtegio(self): # esto es un método protegido porque tiene simple guión bajo
		print("Nombre: ", self.nombre)
		print("Apellido Paterno:", self._apeP)
		print("Apellido Materno:", self.__apeM)

	def __metodoPrivado(self): # No se pueden acceder a los atributos desde este método porque es privado
		print("Nombre: ", self.nombre)
		print("Apellido Paterno:", self._apeP)
		print("Apellido Materno:", self.__apeM)

# métodos getters y setters		

	def getNombre(self):
		return self.nombre

	def setNombre(self,nombre):
		self.nombre = nombre

	def get_apeP(self):
		return self._apeP

	def set_apeP(self,apellidoPaterno):
		self._apeP = apellidoPaterno

	def get_apeM(self):
		return self.__apeM

	def set_apeM(self,apellidoMaterno):
		self.__apeM = apellidoMaterno						
			


persona = Persona("Gustavo","Palacios","Meyer")
persona2 = Persona("María","Rodriguez", "Montenegro")
persona2._metodoProtegio()	
# persona.__metodoPrivado()	
persona.metodoPublico()	
print("##################")
print(persona.getNombre())
print(persona.get_apeP())
print(persona.get_apeM())



