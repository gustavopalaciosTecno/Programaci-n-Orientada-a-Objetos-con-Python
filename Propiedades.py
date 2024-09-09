class Persona:
    def __init__(self,nombre,apellidos):
        self.__nombre = nombre
        self.__apellidos = apellidos
    
    @property    
    def nombre(self):
        return f"Nombre: {self.__nombre}"
    
    @property
    def apellidos(self):
        return f"Apellidos: {self.__apellidos}"
    
    @apellidos.deleter
    def apellidos(self):
        del self.__apellidos
    
    @nombre.setter # con este decorador podemos modificar el nombre
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
        

persona1 = Persona("Gustavo","Palacios Meyer")

nombre = persona1.nombre
print(nombre)
persona1.nombre = "Florencia"
print(persona1.nombre)
apellidos = persona1.apellidos
print(apellidos)

del persona1.apellidos
# print(persona1.apellidos)
print("Hello")
