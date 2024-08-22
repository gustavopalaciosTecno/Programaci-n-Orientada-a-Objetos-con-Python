# Ejercicio 1: Números Pares
# Problema: Escribe una función que reciba una lista de números enteros y retorne una nueva lista con solo los números pares.

def Numeros(lista):
    for item in lista:
        if item % 2 == 0:
            print(f"es un valor par: {item}")
            
            
Numeros([1,2,3,4,5,6,7,8,9,10,11,12])

# Convertir la función en un método dentro de una clase
class NumerosPares:
    def SoloNumerosPares(self,lista):
        for item in lista:
            if item % 2 == 0:
                print(f"es un valor par: {item}")
            
pares = NumerosPares()
pares.SoloNumerosPares([13,14,15,16,17,18,19,20,21,22])            
    
  
            
            