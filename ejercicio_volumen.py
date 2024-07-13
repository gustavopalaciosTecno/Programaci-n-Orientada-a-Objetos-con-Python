print("###################CALCULAR EL VOLUMEN ######################")
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
#se agregan dos formas de imprimir en pantalla # print("el volumen de la caja es: ", cajita.calcularVolumen())	
print(f"el valor del volumen de la caja es: {round((cajita.calcularVolumen()))}")			

print("####################### CALCULAR OPERACIONES ARTIMÉTICAS ########################")

class Calculadora:
	def __init__(self,valor1,valor2):
		self.valor1 = valor1
		self.valor2 = valor2

	def sumarValores(self,resultado1):
		self.resultado1 = self.valor1 + self.valor2
		print(f"el resultado de sumar: {self.valor1} con {self.valor2} es {self.resultado1}")

	def restarValores(self,resultado1):
		self.resultado1 = self.valor1 - self.valor2
		print(f"el resultado de restar: {self.valor1} con {self.valor2} es {self.resultado1}")

	def multiplicarValores(self,resultado1):
		self.resultado1 = self.valor1 * self.valor2
		print(f"el resultado de multiplicar: {self.valor1} con {self.valor2} es {self.resultado1}")

	def dividirValores(self,resultado1):
		self.resultado1 = self.valor1 / self.valor2
		print(f"el resultado de dividir: {self.valor1} con {self.valor2} es {self.resultado1}")
    	
    	

opciones = int(input("Coloca un número para realizar la operación: "))		
valor1 = float(input("coloca primer valor: "))
valor2 = float(input("Coloca segundo valor: "))

suma = Calculadora(valor1,valor2)
resta = Calculadora(valor1,valor2)
producto = Calculadora(valor1,valor2)
cociente = Calculadora(valor1,valor2)
resultado1 = None

if opciones == 1:
	suma.sumarValores(resultado1)
elif opciones == 2:
	suma.restarValores(resultado1)	
elif opciones == 3:
	producto.multiplicarValores(resultado1)
elif opciones == 4:
	cociente.dividirValores(resultado1)
else:	
	print("Coloca un número válido para realizar la operación !")			