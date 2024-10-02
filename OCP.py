#Principio de abierto/cerrado
"""
las entidades de software(clase, métodos, etc) tiene que estar abiertas para la extensión, pero cerrdas para la modificación
se podría agregar nuevas funcionalidades, pero sin modificar el código, sino extenderlo.
"""
class Notificador:
    def __init__(self,usuario,mensaje):
        self.usuario = usuario
        self.mensaje = mensaje
    
    def notificar(self):
        raise NotImplementedError

class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"enviando mensaje por mail al {self.usuario.email}")  
        
class NotificadorSms(Notificador):
    def Notificar(self):
        print(f"enviando mensaje sms al {self.usuario.sms}")        
               
 
