from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
           pass 
       
    def presentarse(self):
        print(f"hola me llamo {self.nombre} y mi edad es de {self.edad} años de edad")
        
        
class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad) 
               

    def hacer_actividad(self):
        print(f"estoy haciendo {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad,sexo,actividad) 
                      

    def hacer_actividad(self):
        print(f"actualmente estoy trabajando en el rubro {self.actividad}")        
               
gustavo = Estudiante("Néstor",43,"masculino","programación")
gustavo.hacer_actividad()   
       
           
        