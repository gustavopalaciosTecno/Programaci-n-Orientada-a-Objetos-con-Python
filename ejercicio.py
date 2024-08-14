class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        return "Me encuentro estudiando !"
    
nombre = input("Agregar nombre: ")    
edad = int(input("Agregar edad: "))
grado = input("Agregar grado: ")    

estudiante = Estudiante(nombre,edad,grado)

print(f"""
      Nombre: {estudiante.nombre}\n
      Edad: {estudiante.edad}\n
      Grado: {estudiante.grado}
      """)
estudiar = input("pone estudiar...: ")
         
if estudiar.lower() == "estudiar":
    print(estudiante.estudiar())    