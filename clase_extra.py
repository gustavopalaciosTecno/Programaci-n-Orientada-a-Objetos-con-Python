class Persona:
	def __init__(this,n,e,*v,**d): # Se puede agregar this al código,pero lo recomendable es usar self
							   # con el asterisco y el nombre de la variable se crea una tupla
		this.nombre = n        # con el doble asterisco creamos un diccionario
		this.edad = e
		this.valores = v
		this.diccionario = d

	def desplegar(self): # Es posible agregar self al crear un nuevo método
		print("Nombre: ", self.nombre)
		print("Edad:", self.edad)	
		print("Valores: tupla()", self.valores)
		print("Diccionario: ", self.diccionario)

p1 = Persona("Maria",36)
p2 = Persona("Gustavo",43)
print("\n")
print("Nombre:\n",p1.nombre)
print("Edad:\n",p1.edad)
print("Nombre:\n",p2.nombre)
print("Edad:\n",p2.edad)	
print("\n")
# ahora llamamos al método desplegar
p1.desplegar()
p2.desplegar()	
print("\n")
# creamos otro objeto para mostrar la tupla
p3 = Persona("Lidia",36,15,14,9)
p3.desplegar()
print("\n")
# creamos otro objeto para mostrar el diccionario
p4 = Persona("Ricardo",54,8,9,f="Enfermero del hospital",p="Profesor de la UNNE")
p4.desplegar()