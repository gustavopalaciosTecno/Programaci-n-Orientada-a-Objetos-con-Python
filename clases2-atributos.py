class Gato:
	numero_patas = 4
	cantidad_orejas = 2
	nombres = []
	def __init__(self,nombre):
		self.nombre = nombre
		self.nombres.append(nombre)

garfield = Gato("Garfield")
bigotes = Gato("Bigotes")
print(garfield.numero_patas)
print(garfield.cantidad_orejas)
print(bigotes.numero_patas)
print(bigotes.cantidad_orejas)

# accedemos a la clase directamente y llamamos al objeto nombres
print(Gato.nombres) # me muestra los nombres creados de los gatos
# modificamos el valor
Gato.nombres = ["Juancito"]
# imprimos en pantalla accediendo al atributo nombres que es una lista donde agregamos el valor
print(garfield.nombres)
# volvemos hacer nuevamente el cambio
Gato.nombres = ["Pedrito"]
print("el gato se llama", garfield.nombres)
print(bigotes.nombres) # al cambiar el atributo de nombres, se me cambió para todos lso objetos
Gato.nombres = ["Juancito","Pedrito"]
print(Gato.nombres) # imprimo los dos nombres que cree
print(garfield.nombres) # se agregan los dos valores a cada objeto
print(bigotes.nombres) # se agregan los dos valores a cada objeto