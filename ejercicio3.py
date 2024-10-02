class Personaje:
    def __init__(self,nombre,fuerza,velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f"nombre: {self.nombre} - fuerza: {self.fuerza} - velocidad: {self.velocidad}"
    
    def __add__(self,otro_pj):
        nuevo_nombre = self.nombre + "_" + otro_pj.nombre
        nueva_fuerza = ((self.fuerza + otro_pj.fuerza)/2)**2
        nueva_velocidad = ((self.velocidad + otro_pj.velocidad)/2)**2
        return Personaje(nuevo_nombre,nueva_fuerza,nueva_velocidad)
      
    
    
goku = Personaje("goku",100,200)
superSayayin = Personaje("SuperSayayin",150,300)

nuevo_personaje = goku +  superSayayin
print(nuevo_personaje.nombre)  
print(nuevo_personaje.fuerza)  
print(nuevo_personaje.velocidad)  