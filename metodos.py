# Artimética

class Aritmetica:
	def __init__(self,valor1,valor2):
		self.valor1 = valor1
		self.valor2 = valor2

	def sumar(self):
		""" se realiza la operación con los atributos de la clase"""
		return self.valor1 + self.valor2


# se crea el objeto
artimetica = Aritmetica(150,100)

# se imprime el objeto y se muestra en pantalla
print("el valor de la suma es: ",artimetica.sumar())		

