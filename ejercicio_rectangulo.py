class Rectangulo:
	def __init__(self,base,altura):
		self.base = base
		self.altura = altura

	def calcularArea(self):
		return self.base * self.altura

# una vez creada las variables, pido en pantalla los valores al usuario
base = float(input("Coloca un valor para la base: "))					
altura = float(input("Coloca un valor para la altura: "))

rect = Rectangulo(base,altura)
# agrego round para redondear el valor
print("el valor del área del rectángulo es: ", round(rect.calcularArea()))


