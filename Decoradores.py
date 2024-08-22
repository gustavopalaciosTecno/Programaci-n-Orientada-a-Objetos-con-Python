def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
    return funcion_modificada


@decorador
def saludo():
    print("Hola como estas Gustavo")
    
    
saludo()             