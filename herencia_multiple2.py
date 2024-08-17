import numpy as np
import random
# class Array:
#     def __init__(self,arreglo):
#         self.arreglo = arreglo
        
    
#     def __str__(self):
#         return f"Array: {self.arreglo}"
    
# arr = np.array([15,14,25,99,88,101])
# arreglo = Array(arr)
# print(arreglo)    

class ArrayEntero:
    
    def ejecutarArray(self):
        valor = int(input("Coloca un valor para el rango: "))
        a = [random.randint(0,100) for _ in range(valor)]
        media = np.array(a)
        return (media)
    
    
ejecutar = ArrayEntero()
print(ejecutar.ejecutarArray())
    
    

        
    


