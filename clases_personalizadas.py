class Corredor:
    __numeros_usados = set()

    def __new__(cls, nombre, num=1):
        while num in cls.__numeros_usados:
            num += 1

        cls.__numeros_usados.add(num)
        instancia = super(Corredor, cls).__new__(cls)
        instancia.__init__(nombre)
        instancia.num = num
        return instancia			

    def __init__(self, nombre):
        self.nombre = nombre

    def __del__(self):
        self.__numeros_usados.remove(self.num)


juan = Corredor('Juan')
maria = Corredor('Maria')
ana = Corredor('Ana')
print(juan.num)
print(maria.num)
print(ana.num)
print(f"\nnombre:{juan.nombre}\nnombre:{maria.nombre}\nnombre:{ana.nombre}")
del maria



