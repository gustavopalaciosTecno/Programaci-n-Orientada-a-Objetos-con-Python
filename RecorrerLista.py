class Lista:
    def recorrerLista(self,lista):
        for item in lista:
            print(f"el elemento actual de la lista es: {item}")
            
            
elemento1 = [1,2,3,4,5,6,7,8,9,10]
elemento2 = ["Nestor","Lidia","Roberto","Macarena"]

listado = Lista()
listado.recorrerLista(elemento1)   
print("\n")  
listado.recorrerLista(elemento2)            
    

