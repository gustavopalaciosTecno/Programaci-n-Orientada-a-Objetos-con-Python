# Ejercicio 4: Suma de Dígitos
# Problema: Escribe una función que sume los dígitos de un número entero.

def suma_digitos(n):
    return sum(int(digitos) for digitos in str(n))

numeros = 12345
resultado = suma_digitos(numeros)
print(numeros)

# Lo pasamos a clases
class Digitos:
    def suma_digitos(self,n):
        return sum(int(digitos) for digitos in str(n))
    

numeros = 12345
resultado = Digitos()
print(resultado.suma_digitos(numeros))    