class Persona:
    def __init__(self,nombre,apellidos):
        self.__nombre = nombre
        self.__apellidos = apellidos
        
    def get_Nombre(self):
        return f"Nombre: {self.__nombre}"
    
    def set_Nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
        
    def get_Apellidos(self):
        return f"Apellidos: {self.__apellidos}"
    
    def set_Apellidos(self,nuevo_apellidos):
        self.__apellidos = nuevo_apellidos  
        

persona1 = Persona("Gustavo","Palacios")
print(persona1.get_Nombre())
print(persona1.get_Apellidos())

persona1.set_Nombre("Lidia")
persona1.set_Apellidos("Ruiz")
print(persona1.get_Nombre())
print(persona1.get_Apellidos())
