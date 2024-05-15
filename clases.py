class Coche:
	def __init__(self,color,marca,modelo):
		self.color = color
		self.marca = marca
		self.modelo = modelo

	def mostrarInfo(self):
		return f"el color es: {self.color}-la marca es: {self.marca} - y el modelo es: {self.modelo}"	



coche = Coche("rojo","Volskwagen","1994")
print(coche.mostrarInfo())	

#se accede directamente al atributo	
print(coche.color) 
print(coche.marca)
print(coche.modelo)

# otra forma de imprimri los valores
resultado = f"color: {coche.color} - marca: {coche.marca} - modelo: {coche.modelo}" 
print(resultado)