import os
class Cifrado_Simetrico:
    def __init__(self, mensaje, clave):
        self.mensaje = mensaje
        self.clave = clave
    def getMensaje(self):
        return self.mensaje
    def getClave(self):
        return self.clave

    def cifrar(self):
        cadenaCifrada = ""
        
          
    def descifrar(self, mensajeCifrado):
        mensajeDescifrado = ""
        

os.system('cls')
mensaje = input("Introduzca el mensaje: ")
clave = input("Introduzca la clave: ")
objeto = Cifrado_Simetrico(mensaje, clave)
resultadoCifrado = objeto.cifrar()
objeto.descifrar(resultadoCifrado) 