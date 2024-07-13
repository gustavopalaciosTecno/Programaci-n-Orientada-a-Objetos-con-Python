class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def sumar(self):
        return self.valor1 + self.valor2

    def restar(self):
        return self.valor1 - self.valor2

    def multiplicar(self):
        return self.valor1 * self.valor2

    def dividir(self):
        if self.valor2 != 0:
            return self.valor1 / self.valor2
        else:
            return "Error: División por cero"


# usamos método main              

def main():
    try:  
        print("Opciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
  
        opcion = int(input("Elegí una opción (1-4): "))
        valor1 = float(input("Ingresa el primer valor: "))
        valor2 = float(input("Ingresa el segundo valor: "))

        calculadora = Calculadora(valor1, valor2)

        if opcion == 1:
            resultado = calculadora.sumar()
            operacion = "sumar"
        elif opcion == 2:
            resultado = calculadora.restar()
            operacion = "restar"
        elif opcion == 3:
            resultado = calculadora.multiplicar()
            operacion = "multiplicar"
        elif opcion == 4:
            resultado = calculadora.dividir()
            operacion = "dividir"
        else:
            print("Opción no válida")
            return

        print(f"El resultado de {operacion} {valor1} y {valor2} es {resultado}")

    except ValueError:
        print("Error: Entrada no válida. Por favor, ingresa un número.")   
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    main()


        