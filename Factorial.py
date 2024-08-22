# Ejercicio 2: Factorial de un Número
# Problema: Escribe una función que calcule el factorial de un número entero no negativo.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
try:    
    numero = int(input("Coloca un número para saber el factorial: "))
    resultado = factorial(numero)
    print(f"el factorial de {numero} es {resultado}")
except Exception as error:    
    print("Se produjo un error de tipeo",error)
    
# Pasar a clase
class numeroFactorial:
    def factorial(self,n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n-1)
try:    
    numero = int(input("Coloca un número para saber el factorial: "))
    factor = numeroFactorial()
    resultado = factor.factorial(numero)
    print(f"el factorial de {numero} es {resultado}")
except Exception as error:    
    print("Se produjo un error de tipeo",error)


    
        
    