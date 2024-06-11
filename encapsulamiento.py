class Animal:
	def __init__(self,nombre):
		self.__nombre = nombre
		self.especie = "vertebrado" # se agrega un atributo sin agregarlo como parámetro

	def get_nombre(self):
		return self.__nombre

	def set_nombre(self,nombre):
		self.__nombre = nombre

	def get_especie(self):
		return self.especie

	def set_especie(self,especie):
		self.especie = especie		


a1 = Animal("Jirafa")
#print(a1.__nombre) no se puede acceder al atributo privado de esta forma
print(a1.get_nombre())
# cambiar un atributo privado usando set
a1.set_nombre("Leon")
print(a1.get_nombre())

print(a1.get_especie())