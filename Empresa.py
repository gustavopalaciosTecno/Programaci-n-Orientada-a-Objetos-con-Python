class Director:
    def __init__(self, nombre, apellidos, email, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellidos: {self.apellidos}\nCorreo: {self.email}\nEdad: {self.edad}"

    def gestionar_tareas(self):
        return "Realizar tareas de gestión"

class Vicedirector(Director):
    def __init__(self, nombre, apellidos, email, edad, tareas_secundarias):
        super().__init__(nombre, apellidos, email, edad)
        self.tareas_secundarias = tareas_secundarias

    def __str__(self):
        return super().__str__() + f"\nTareas secundarias: {self.tareas_secundarias}"

    def recibe_ordenes(self):
        return "Recibe órdenes del director"

class Secretario(Director):
    def __init__(self, nombre, apellidos, email, edad, administra):
        super().__init__(nombre, apellidos, email, edad)
        self.administra = administra

    def __str__(self):
        return super().__str__() + f"\nAdministra: {self.administra}"

class JefeAuxiliarDocentes(Director):
    def __init__(self, nombre, apellidos, email, edad, funcion):
        super().__init__(nombre, apellidos, email, edad)
        self.funcion = funcion

    def __str__(self):
        return super().__str__() + f"\nFunción: {self.funcion}"

class Docente(Director):
    def __init__(self, nombre, apellidos, email, edad, cant_catedras):
        Director.__init__(self, nombre, apellidos, email, edad)
        self.cant_catedras = cant_catedras

    def __str__(self):
        return super().__str__() + f"\nTotal cátedras: {self.cant_catedras}"

class AuxiliarDocente(Docente, JefeAuxiliarDocentes):
    def __init__(self, nombre, apellidos, email, edad, cargo, cant_catedras, funcion):
        # Inicializa Docente explícitamente
        Docente.__init__(self, nombre, apellidos, email, edad, cant_catedras)
        # Inicializa JefeAuxiliarDocentes explícitamente
        JefeAuxiliarDocentes.__init__(self, nombre, apellidos, email, edad, funcion)
        self.cargo = cargo
        
    def __str__(self):
        return Docente.__str__(self) + f"\nCargo: {self.cargo}" + f"\nFunción: {self.funcion}"

# Ejemplo de uso
auxiliar = AuxiliarDocente("Lidia", "Ruiz", "lidia@mail.com", 44, "auxiliar", 18, "administrativa")
print(auxiliar)
