class Persona:
	def __init__(self,nombre,edad):
		self.nombre = nombre
		self.edad = edad

			
	

#modificar los valores
Persona.nombre = "Gustavo"
Persona.edad = 43

#Acceder a los valores
print(Persona.nombre)
print(Persona.edad)

# Creación de un objeto
persona = Persona("María",36)
print(persona.edad)
print(persona.nombre)

# Imprimir valores en pantalla en una sola línea
print(f"vos te llamas {(persona.nombre)} y tu edad es: {(persona.edad)} años")

# Creación de un segundo objeto
persona2 = Persona("Albana",31)
print(f" te llamas: {(persona2.nombre)} y tenes {(persona2.edad)} años de edad")

