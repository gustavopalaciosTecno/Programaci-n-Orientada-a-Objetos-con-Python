class Punto:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def getx(self):
 		return self._x

	def setx(self,valor):
 		raise Exception('Valor x no puede ser modificado')	

	def delx(self):
 		del self._x		

	x = property(getx, setx, delx, 'posición en el eje de las abscisas')	

	def getx(self):
		return self._y

	def sety(self,valor):
		self._y = valor

	def dely(self):
		raise Exception('el atributo (y) no puede ser eliminado')

	y = property(getx,setx,delx, 'posición en el eje de las ordenadas')	


p1 = Punto(4,2)
p1.x,p1.y
p1.x = 90
p1.y = 50



