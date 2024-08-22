class Persona:
    def __init__(self,nombre,apellidos):
        self.__nombre = nombre
        self.__apellidos = apellidos
    
    @property    
    def nombre(self):
        return f"Nombre: {self.__nombre}"
    
    
        

persona1 = Persona("Gustavo","Palacios")

nombre = persona1.nombre
print(nombre)
