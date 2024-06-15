class Director:
	def __init__(self,nombre,colegio,sueldo,funcion):
		self.nombre = nombre
		self.colegio = colegio
		self.sueldo = sueldo
		self.funcion = funcion

	def __str__(self):
		return "Nombre: " + self.nombre + "\nColegio:" + self.colegio + "\nSueldo:" + str(self.sueldo) + "\nFunción:" + self.funcion


class DocenteHoras(Director):
	def __init__(self,nombre,colegio,sueldo,funcion,dictado):
		super().__init__(nombre,colegio,sueldo,funcion)
		self.dictado = dictado

	def __str__(self):
		return super().__str__() + "\nDictado: " + self.dictado	

class Secretario(Director):
	def __init__(self,nombre,colegio,sueldo,funcion,administrar):
		super().__init__(nombre,colegio,sueldo,funcion)
		self.administrar = administrar	
	def __str__(self):
		return super().__str__() + "\nAdministrar:" + self.administrar	

dire = Director("Marcelo","E.E.S N°23",900000,"Gestionar institución")
print(dire)					
docente1 = Director("Gustavo","E.E.S N23",860000,"Dictar clases")
print(docente1)
docente2 = Secretario("Paola","E.E.S N23",820000,"gestionar","administrar escuela")
print(docente2)