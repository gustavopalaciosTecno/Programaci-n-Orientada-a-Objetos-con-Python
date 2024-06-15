class Calculadora:
	def __init__(self,valor1,valor2):
		self.valor1 = valor1
		self.valor2 = valor2

	def sumarValor(self):
		self.valor1=float(input("Coloca primer valor: "))
		self.valor2 = float(input("Coloca segundo valor: "))
		resultado = self.valor1 + self.valor2
		print(f"el resultado de sumar: {(self.valor1)} y {(self.valor2)} es {resultado}")

	def restarValor(self):
		self.valor1=float(input("Coloca primer valor: "))
		self.valor2 = float(input("Coloca segundo valor: "))
		resultado2 = self.valor1 - self.valor2	
		print(f"el resultado de restar: {(self.valor1)} y {(self.valor2)} es {resultado2}")

	def multiplicarValor(self):
		self.valor1=float(input("Coloca primer valor: "))
		self.valor2 = float(input("Coloca segundo valor: "))
		resultado3 = self.valor1 * self.valor2	
		print(f"el resultado de multiplicar: {(self.valor1)} y {(self.valor2)} es {resultado3}")

	def dividirValores(self):
		self.valor1=float(input("Coloca primer valor: "))
		self.valor2 = float(input("Coloca segundo valor: "))
		resultado4 = self.valor1 / self.valor2
		print(f"el resultado de multiplicar: {(self.valor1)} y {(self.valor2)} es {resultado4}")	
			

	def opcionesValores(self):
		opcion = int(input("Elegí un número para realizar la operación: "))	
		if opcion == 1:
			print("Elegiste la opción se sumar los valores")
			self.sumarValor()
		elif opcion == 2:
			print("Elegiste la opción se restar los valores")
			self.restarValor()
		elif opcion == 3:
			print("Elegiste la opción se multiplicar los valores")
			self.multiplicarValor()
		elif opcion == 4:
			print("Elegiste la opción de dividir los valores")
			self.dividirValores()	
		else:
			print("Elegí la opción correcta")		



cal = Calculadora(valor1=0,valor2=0)
cal.opcionesValores();
	



