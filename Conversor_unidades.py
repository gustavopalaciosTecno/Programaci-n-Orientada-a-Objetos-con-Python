class ConversorTemperatura:
    def __init__(self,escala,valor):
        self.escala = escala
        self.valor = valor
        
    def convertir(self):
        if self.escala == "C":
            resultado = (self.valor - 32) * 5/9
            return f"{resultado} grados Celsius"
        elif self.escala == "F":
            resultado = (self.valor * 9/5)+32 
            return f"{resultado} grados Farenheit"
        else:
            return "Valor no contemplado"
        
try:        
    escala = input("Introduci la letra C(celsius) o la letra F(Farenheit): ").upper()
    valor = float(input("introducí un valor: "))
    conver = ConversorTemperatura(escala,valor)
    print(conver.convertir())    
except Exception as e:
    print("Se produjo un error",e)

  
            