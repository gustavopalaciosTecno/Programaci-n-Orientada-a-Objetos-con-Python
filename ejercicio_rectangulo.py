class Rectangulo:
	def __init__(self,base,altura):
		self.base = base
		self.altura = altura

	def calcularArea(self):
   		return self.base * self.altura	

   	
 
rect = Rectangulo(8,12)
print("el valor del area es: ",rect.calcularArea())    			