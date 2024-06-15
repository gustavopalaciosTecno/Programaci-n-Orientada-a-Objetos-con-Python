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
			


persona = Persona("Gustavo","Palacios","Meyer")
persona2 = Persona("María","Rodriguez", "Montenegro")
persona2._metodoProtegio()	
# persona.__metodoPrivado()	
persona.metodoPublico()	