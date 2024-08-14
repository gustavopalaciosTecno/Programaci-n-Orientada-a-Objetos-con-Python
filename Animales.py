class Cordados:
    def __init__(self,subtipo,clase,orden,familia):
        self.subtipo = subtipo
        self.clase = clase
        self.orden = orden
        self.familia = familia
        
     
    def __str__(self):
        return (f"Subfilum: {self.subtipo}\nClase: {self.clase}\nOrden: {self.orden}\nFamilia: {self.familia}")
    
class Vertebrados(Cordados):
    def __init__(self,subtipo,clase,orden,familia,genero,especie):
        super().__init__(subtipo,clase,orden,familia)  
        self.genero = genero
        self.especie = especie
    
    def __str__(self):
        return super().__str__() + " Género: " + self.genero + " Especie: " + self.especie
    
subtipo = input("Coloca el filum: ")              
clase = input("Coloca una clase: ")
orden = input("Coloca el orden: ")
familia = input("Coloca la familia: ")
genero = input("Pone el género: ")
especie= input("¿Qué especie es?: ")

animal1 = Vertebrados(subtipo,clase,orden,familia,genero,especie)
print(animal1)