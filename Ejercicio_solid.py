# class Calculos:
#     def __init__(self,valor1,valor2):
#         self.valor1 = valor1
#         self.valor2 = valor2
      
#     def elegirOpciones(self):
#         self.opcion = int(input("Elegí una opcion: "))
#         if self.opcion == 1:
#             self.realizarSuma()
#         elif self.opcion == 2:
#             self.realizarResta()
#         elif self.opcion == 3:
#             self.realizarProducto() 
#         elif self.opcion == 4:
#             self.realizarCociente() 
#         else:
#             return "No se puede realizar la operación"             
            
#     def realizarSuma(self):
#         print("el resultado de la suma es: ",self.valor1 + self.valor2) 
               
        
#     def realizarResta(self):
#         print("el resultado de la resta es: ",self.valor1 - self.valor2) 
            
#     def realizarProducto(self):
#         print("el resultado de la multiplicación es: ",self.valor1 * self.valor2) 
        
#     def realizarCociente(self):
#         print("el resultado de la división es: ",self.valor1 // self.valor2)                                       

  
            
# calcular = Calculos(15,20) 
# calcular.elegirOpciones()


# class Lista:
#     def __init__(self):
#         self.miLista = []
        
#     # def agregarValores(self,valores):
#     #     self.miLista.append(valores)
#     agregarValores = lambda self,valores:self.miLista.append(valores)
    
#     def __str__(self):
#         return f"los valores que se agregaron son los siguientes: {self.miLista}" 
    
# lista = Lista()
# lista.agregarValores(15)       
# lista.agregarValores(150)     
# lista.agregarValores(45) 
# print(lista)    

# contador = 0

# while contador < 5:
#     print("""
#     Elige una opción:
#     1. Sumar
#     2. Restar
#     3. Multiplicar
#     4. Dividir
#     5. Salir
#     """)
    
#     try:
#         opciones = int(input("Introduce una opción entre (1-5): "))  # Pide al usuario que ingrese una opción
        
#         if opciones == 1:
#             valor1 = float(input("Ingrese primer valor: "))
#             valor2 = float(input("Ingrese segundo valor: "))
#             resultado = valor1 + valor2
#             print(f"El resultado de la suma es: {resultado}")
        
#         elif opciones == 2:
#             valor1 = float(input("Ingrese primer valor: "))
#             valor2 = float(input("Ingrese segundo valor: "))
#             resultado = valor1 - valor2
#             print(f"El resultado de la resta es: {resultado}")
        
#         elif opciones == 3:
#             valor1 = float(input("Ingrese primer valor: "))
#             valor2 = float(input("Ingrese segundo valor: "))
#             resultado = valor1 * valor2
#             print(f"El resultado de la multiplicación es: {resultado}")
        
#         elif opciones == 4:
#             valor1 = float(input("Ingrese primer valor: "))
#             valor2 = float(input("Ingrese segundo valor: "))
#             if valor2 != 0:
#                 resultado = valor1 / valor2
#                 print(f"El resultado de la división es: {resultado}")
#             else:
#                 print("Error: No se puede dividir por 0.")
        
#         elif opciones == 5:
#             print("Saliendo del programa...")
#             break
        
#         else:
#             print("Opción no válida. Por favor, elige entre 1 y 5.")
    
#     except ValueError:
#         print("Error: Por favor ingresa un número válido.")
    
#     contador += 1

                      
        
# print("Escuela de Educación Secundaria N° 23 \"José Chudnovsky\"")
    

  
        
            
            
            
            
        
        