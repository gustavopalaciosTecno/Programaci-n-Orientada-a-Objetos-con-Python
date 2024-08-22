# Ejercicio 3: Palíndromo
# Problema: Escribe una función que determine si una cadena de texto es un palíndromo (se lee igual de adelante hacia atrás).

def es_palindromo(cadena):
    cadena = cadena.replace(" ","").lower()
    return cadena == cadena[::-1]


texto = input("escribi un texto acá: ")
es_palindromo_resultado = es_palindromo(texto)
if es_palindromo_resultado == True:
    print(f"la palabra {texto} es un palíndromo")
elif es_palindromo_resultado == False:
    print(f"la palabra {texto} NO es un palíndromo")  
      
    







