# Ejercicio 5: Números Primos
# Problema: Escribe una función que determine si un número entero es primo.


class Primos:
    def es_primo(self,n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

# Ejemplo de uso
numero_primo = int(input("Coloca un valor para saber si es primo: "))
resultado_primo = Primos()
if resultado_primo == True:
    print(f"El número {numero_primo} es primo")
    nuevo_resultado = resultado_primo.es_primo(numero_primo)
else:    
    print("no es primo")


   