class Tarea:
    def __init__(self):
        self.tareas = []

    def listarTarea(self):
        if not self.tareas:
            print("No hay tareas.")
        else:
            print("Las tareas son las siguientes:")
            for i, tarea in enumerate(self.tareas, start=1):
                print(f"{i}. {tarea}")

    def agregarTarea(self):
        agregar = input("Agrega una tarea acá: ")
        self.tareas.append(agregar)
        print(f"La tarea '{agregar}' ha sido agregada.")

    def editarTarea(self):
        self.listarTarea()
        if self.tareas:
            try:
                numero = int(input("Elige el número de la tarea que quieres editar: "))
                if 1 <= numero <= len(self.tareas):
                    nueva_tarea = input("Escribe la nueva tarea: ")
                    self.tareas[numero - 1] = nueva_tarea
                    print(f"La tarea número {numero} ha sido actualizada.")
                else:
                    print("Número de tarea no válido.")
            except ValueError:
                print("Por favor, introduce un número válido.")

    def borrarTarea(self):
        self.listarTarea()
        if self.tareas:
            try:
                numero = int(input("Elige el número de la tarea que quieres borrar: "))
                if 1 <= numero <= len(self.tareas):
                    tarea_borrada = self.tareas.pop(numero - 1)
                    print(f"La tarea '{tarea_borrada}' ha sido borrada.")
                else:
                    print("Número de tarea no válido.")
            except ValueError:
                print("Por favor, introduce un número válido.")

    def guardarTarea(self):
        with open("tareas.txt", "w") as archivo:
            for tarea in self.tareas:
                archivo.write(tarea + "\n")
        print("Las tareas han sido guardadas en 'tareas.txt'.")


tar = Tarea()


tar.listarTarea()
tar.agregarTarea()
tar.listarTarea()
tar.editarTarea()
tar.borrarTarea()
tar.guardarTarea()
		
