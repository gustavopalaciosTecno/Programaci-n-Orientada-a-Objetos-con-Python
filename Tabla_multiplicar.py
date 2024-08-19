import math
class Tablas:
    def __init__(self,valor):
         self.valor = valor        
    
    def extraerTabla(self):
        contador = 0
        for i in range(11):
            print(f"{self.valor} * {contador} = {self.valor * contador}")
            contador += 1
    def extraerPotencias(self):
        cuadrado = math.pow(self.valor,2)
        cubo = math.pow(self.valor,3)
        print(f"el valor que colocaste en consola al cuadrado es: {cuadrado}\ny al cubo es: {cubo}")
    def extraerCircunferencia(self):
            circunferencia = 2 * math.pi * self.valor
            print(f"la circunferencia de la circunferencia es: {circunferencia}")
 
valor = int(input("Coloca un valor para realizar la tabla y las potencias: ")) 

class Cuadrados(Tablas):
    def __init__(self,valor):
        super().__init__(valor)

class Cricunferencia(Tablas):
      def __init__(self,valor):
            super().__init__(valor)
        
          
calcular = Tablas(valor)  
calcular.extraerTabla()
calcular.extraerPotencias()
calcular.extraerCircunferencia()  

