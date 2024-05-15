class Medida:
	_atributoProtegido = 0
	__atributoPrivado = 0

	def __init__(self,x):
		self.x = x
		self._x = x * 2
		self.__x = x * 3

	def obtener_x(self):
		return self.x

	def obtenerAtributoProtegido(self):

		return self._x

	def obtenerAtributoPrivado(self):
		return self.__x	




med = Medida(2);
print(med.x)
print(med._x) # obtiene atriobuto protegido
#print(med.__x) no se puede acceder al método privado
print(dir(med)) # usamos la función dir para ver un listado por defecto de los atributos

