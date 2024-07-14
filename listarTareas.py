class Tarea:
	def __init__(self,listar,guardar,editar):
		self.listar = listar
		self.guardar = guardar
		self.editar = editar


	def listarTarea(self):
			tarea = []
			print(f"las tareas son las siguientes: {tarea}")

	def agregarTarea(self):
			tarea = []
			agregar = input("agrega una tarea acá: ")
			tarea.append(agregar)
			print(f"la tarea es la siguiente: {agregar}")

listar = " "
guardar = " "
editar = " "

tar = Tarea(listar,guardar,editar)
tar.listarTarea()
tar.agregarTarea()			
