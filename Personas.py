class Persona:
    def __init__(self,nombre,apellido,nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        return "Hola, estoy hablando un poco"
    
class Artista:
    def __init__(self,habilidad,edad):
        self.habilidad = habilidad
        self.edad = edad
        
    def mostrar_habilidad(self):
        return (f"mi hablidad es: {self.edad} y tengo {self.habilidad} de edad")
    
class EmpleadoArtista(Persona,Artista):
    def __init__(self,nombre,apellido,nacionalidad,habilidad,edad,salario,empresa):
        Persona.__init__(self,nombre,apellido,nacionalidad)  
        Artista.__init__(self,habilidad,edad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        return (f'{super().mostrar_habilidad()}') 
    
gustavo = EmpleadoArtista("Gustavo","Palacios Meyer","argentina",43,"programar",85000,"stand up")
# print(gustavo.presentarse())  
gustavo = Artista("docente",43)    
herencia = issubclass(EmpleadoArtista,Persona)
instancia = isinstance(gustavo,Artista)
print(herencia)   
print(instancia)                
        