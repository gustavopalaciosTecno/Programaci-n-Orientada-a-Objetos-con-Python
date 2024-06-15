class Vertebrados:
	def __init__(self,nombre,especie,nombreCientifico):
		self.__nombre = nombre
		self.__especie = especie
		self._name = nombreCientifico

	def get_nombre(self):
		return self.__nombre

	def get_especie(self):
		return self.__especie

	def set_nombre(self,nombre):
		self.__nombre = nombre

	def set_especie(self,especie):
		self.__especie = especie

	def get_name(self):
		return self._name

	def set_name(self,nombreCientifico):
		self._name = nombreCientifico		


perro = Vertebrados("firulais","canina","canis familiaris")
print(perro.get_nombre())
print(perro.get_especie())
print(perro.get_name())						
gato = Vertebrados("Garfield","felina","felis familiaris")
print("###############")
print(gato.get_nombre())
print(gato.get_especie())
print(gato.get_name())