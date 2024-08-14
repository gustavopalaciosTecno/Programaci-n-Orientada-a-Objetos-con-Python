class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}\nNacionalidad: {self.nacionalidad}"    
        
class Empleado(Persona):
    def __init__(self,nombre,edad,nacionalidad,cargo): 
        super().__init__(nombre,edad,nacionalidad)
        self.cargo = cargo
    
    def __str__(self):
        return super().__str__() + "\nCargo:" + self.cargo
        
empleado = Empleado(
    nombre=input("Coloca tu nombre: "),
    edad=int(input("Coloca tu edad: ")),
    nacionalidad = input("Coloca tu nacionalidad: "),
    cargo = input("Coloca tu cargo: ")
    )
print(empleado)               