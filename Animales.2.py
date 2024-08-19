class Animal:
    def comer(self):
        print("El animal está comiendo...")
        
class Ave(Animal):
    def volar(self):
        print("El ave está volando...")
        
class Mamifero(Animal):
    def amamantar(self):
        print("El mamífero está amamantando...")                
        
class Murcielago(Ave,Mamifero):
    pass


murcielago = Murcielago()
murcielago.comer()
murcielago.volar()
murcielago.amamantar()
print(Ave.mro())     
 