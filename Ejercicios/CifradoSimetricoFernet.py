from cryptography.fernet import Fernet
import os

class Cifrado_fernet:

    def _init_(self, mensaje, clave=None):
        self.mensaje = mensaje
        self.clave = clave if clave else Fernet.generate_key()
        self.Fernet = Fernet(self.clave)

    def getMensaje(self):
        return self.mensaje

    def getClave(self):
        return self.clave

    def getFernet(self):
        return self.Fernet

    def cifrar(self):
        token = self.getFernet().encrypt(b'hola mundo')
        print("Mensaje cifrado:")
        print(token)
        return token

    def descifrar(self, token):
        mensaje = self.mensaje = self.getFernet().decrypt(token)
        print("Mensaje descifrado:")
        print(mensaje)
        return mensaje

os.system('cls')
objeto = Cifrado_fernet("Hola")
Mensaje_cifrado = objeto.cifrar()
objeto.descifrar(Mensaje_cifrado)