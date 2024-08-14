class Smart:    
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        
    def __str__(self):
        return (f"Marca: {self.marca}\nModelo: {self.modelo}\nPrecio: {self.precio}")    
        
class Samsung(Smart):
    def __init__(self,marca,modelo,precio,detalles):
        super().__init__(marca,modelo,precio)
        self.detalles = detalles
        
    def __str__(self):
        return super().__str__() + "\nDetalles: " + self.detalles + "\n\n"
    
class Motorola(Smart):
    def __init__(self,marca,modelo,precio,detalles):
        super().__init__(marca,modelo,precio)
        self.detalles = detalles
        
    def __str__(self):
        return super().__str__() + "\nDetalles: " + self.detalles 
    
celu1 = Samsung("Samsung","A12",250000,"Nuevo")
print(celu1)
celu2 = Motorola("Motorola","E16",200000,"Usado")
print(celu2)          
                