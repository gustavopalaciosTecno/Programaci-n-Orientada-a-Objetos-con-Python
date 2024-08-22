print("############# CONVERSOR DE MINUTOS A HORAS ##########")

class MinutosAHoras:
    def calcular(self):
        minutos = float(input("Coloca los minutos: "))
        valorMinuto = 0.0167
        hora = (minutos * valorMinuto)
        return(f"los {minutos} minutos corresponde a {hora:.2f} horas")
    
minuto = MinutosAHoras()
print(minuto.calcular())    
        

