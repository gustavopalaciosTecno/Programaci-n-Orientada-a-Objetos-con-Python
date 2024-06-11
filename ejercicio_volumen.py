# Calcular el volumen de una caja
class Caja:
	def __init__(self,largo,ancho,alto):
		self.largo = largo
		self.ancho = ancho
		self.alto = alto

	def calcularVolumen(self):
		return self.largo * self.ancho * self.alto


largo = float(input("Coloca el largo de la caja: "))
ancho = float(input("Coloca el ancho de la caja: "))
alto = float(input("Coloca el alto de la caja: "))

cajita = Caja(largo,ancho,alto)
# se agregan dos formas de imprimir en pantalla
# print("el volumen de la caja es: ", cajita.calcularVolumen())	
print(f"el valor del volumen de la caja es: {(cajita.calcularVolumen())}")			
