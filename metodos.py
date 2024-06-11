# Artimética

class Aritmetica:
	def __init__(self,valor1,valor2):
		self.valor1 = valor1
		self.valor2 = valor2

	def sumar(self):
		""" se realiza la operación con los atributos de la clase"""
		return self.valor1 + self.valor2

	def restar(self):
		return self.valor1 - self.valor2

	def multiplicar(self):
		return self.valor1 * self.valor2

	def dividir(self):
		return self.valor1 // self.valor2			


# Se crea el objeto
artimetica = Aritmetica(150,100)

# Se imprime el objeto y se muestra en pantalla
print("el valor de la suma es: ",artimetica.sumar())
print("el valor de la resta es: ",artimetica.restar())	
print("el valor de la multiplicación es: ",artimetica.multiplicar())	
print("el valor de la división es: ",artimetica.dividir())			

