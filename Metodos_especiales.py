# class Persona:
#     def __init__(self,nombre,edad):
#         self.nombre = nombre
#         self.edad = edad
        
#     def __str__(self):
#         return f'Persona("{self.nombre}",{self.edad})'  
    
#     def __add__(self,otro):
#         nuevo_valor = self.edad + otro.edad
#         return Persona(self.nombre+otro.nombre,nuevo_valor)
    
    
# dalto = Persona("anacleto",78)
# anastasia = Persona("Chicho",120)

# nueva_persona = dalto + anastasia
# print(nueva_persona.edad)     

# class Fraccion:
#     def __init__(self,numerador,denominador):
#         self.numerador = numerador
#         self.denominador = denominador
    
#     def __add__(self,otro):
#         nuevo_numerador = self.numerador * otro.denominador + otro.numerador + self.denominador
#         nuevo_denominador = self.numerador * self.denominador
#         return Fraccion(nuevo_numerador,nuevo_denominador)
    
#     def __repr__(self):
#         return f"Fraccion: {self.numerador}/{self.denominador}"
    
    
# fraccion1 = Fraccion(2,1)
# fraccion2 = Fraccion(9,9)
# resultado = fraccion1 + fraccion2
# print(resultado)        

# class Suma:
#     def __init__(self,valor1,valor2):
#         self.valor1 = valor1
#         self.valor2 = valor2
        
#     def __add__(self,otro):
#         return Suma(self.valor1 + otro.valor1, self.valor2 + otro.valor2)
    
#     def __repr__(self):
#         return f"Sumatoria: {self.valor1}, {self.valor2}"
    
# suma1 = Suma(100,250)
# suma2 = Suma(100,250)
# resultado = suma1 + suma2
# print(resultado)             

class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):    
        return f"tu nombre es : {self.nombre} y tu edad es de {self.edad}"
    
    def __repr__(self):
        return f'Persona("{self.nombre}", {self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre + otro.nombre,nuevo_valor)
    
    
    


gustavo = Persona("Gustavo",43) 
leticia = Persona("Leticia",50)

nueva_persona = gustavo + leticia
print(nueva_persona.edad)
