# MÉTODO SOLID:
# MÉTODO S: PRINCIPIO DE RESPONSABILIDAD ÚNICA (SRP)
""""
UNA CLASE DEBE TENER UNA SOLA RAZÓN PARA CAMBIAR. 
UNA CLASE TIENE QUE REALIZAR UNA SOLA TAREA, Y SI REALIZA OTRA TAREA, 
LA TENEMOS QUE DIVIDIR EN OTRA TAREA.
LA IDEA ES CREAR CLASES SOBRECARGADAS.
"""

class TanqueCombustible:
    def __init__(self):
        self.combustible = 100
    
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible-=cantidad      
    
class Auto:
    def __init__(self,tanque):
        self.posicion = 0
        self.tanque = tanque
    
    def mover(self,distancia):
        if self.tanque.obtener_combustible() >=distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Moviste el auto de forma exitosa")
        else:
            print("No tenes suficiente combustible")

    def obtener_posicion(self):
        return self.posicion 
    
tanque = TanqueCombustible()  
autito = Auto(tanque)      
print(autito.obtener_posicion())
autito.mover(10)               
print(autito.obtener_posicion())
autito.mover(20)   
print(autito.obtener_posicion())
autito.mover(60)  
print(autito.obtener_posicion())
autito.mover(80)  
print(autito.obtener_posicion())
autito.mover(100)  
  

