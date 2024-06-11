class Persona:
	def __init__(this,n,e): # Se puede agregar this al código,pero lo recomendable es usar self

		this.nombre = n
		this.edad = e

	def desplegar(self): # Es posible agregar self al crear un nuevo método
		print("Nombre: ", self.nombre)
		print("Edad:", self.edad)	



p1 = Persona("Maria",36)
p2 = Persona("Gustavo",43)
print("Nombre:\n",p1.nombre)
print("Edad:\n",p1.edad)
print("Nombre:\n",p2.nombre)
print("Edad:\n",p2.edad)	

# ahora llamamos al método desplegar
p1.desplegar()
p2.desplegar()	