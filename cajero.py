class CajeroAutomático:
    def __init__(self, efectivo):
        self.efectivo = efectivo
        
    def mostrarDinero(self):
        print(f"Tu monto es: {self.efectivo} pesos")
        
    def extraerDinero(self, monto):
        if monto > self.efectivo:
            print("No se puede extraer el dinero. Fondos insuficientes.")
        else:
            self.efectivo -= monto
            print(f"pudiste extraer {monto} pesos. Tu nuevo saldo es: {self.efectivo} pesos.")

    def agregarDinero(self, monto):
        self.efectivo += monto
        print(f"Agregaste {monto} pesos. Tu nuevo saldo es: {self.efectivo} pesos.")


cajero = CajeroAutomático(0)


info = """
1. Mostrar dinero
2. Extraer dinero
3. Agregar dinero
4. Salir

"""


contador = 0
while contador != 4:
    print(info)
    opciones = int(input("¿Que deseas realizar?: "))
    if opciones == 1:
        cajero.mostrarDinero()
    elif opciones == 2:
        monto = float(input("¿Cuanto dinero deseas extraer?: "))
        cajero.extraerDinero(monto)
    elif opciones == 3:
        monto = float(input("¿Cuanto dinero deseas agregar?: "))
        cajero.agregarDinero(monto)
    elif opciones == 4:
        break    
    else:
        print("Error al procesar la informacion !")

    contador += 1
