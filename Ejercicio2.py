class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    # def imprimirDatos(self):
    #     return f"Nombre: {self.nombre}\nEdad: {self.edad}"
    def __str__(self):
        return f"Nombre: {self.nombre}\nEdad: {self.edad}"
    
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
    # def imprimirGrado(self):
        # return f"Grado: {self.grado}"
    def __str__(self):
        return super().__str__() + "\nGrado: "  + self.grado  
    
estudiante = Estudiante("Victoria","Miño","3er año")
print(estudiante)
    
                    