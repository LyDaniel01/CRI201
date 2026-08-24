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
        for i in range(len(self.getMensaje())):
            cadenaCifrada += format((ord(self.getMensaje()[i]) ^ ord (clave[i%len(clave)])),"02x")
        print(cadenaCifrada)
        return cadenaCifrada
          
    def descifrar(self, mensajeCifrado):
        mensajeDescifrado = ""
        for i in range(0,len(mensajeCifrado),2):
            mensajeDescifrado += chr(int(mensajeCifrado[i:i+2],16) ^ ord(self.getClave()[i//2 % len(self.getClave())]))
        print(mensajeDescifrado)

os.system('cls')
mensaje = input("Introduzca el mensaje: ")
clave = input("Introduzca la clave: ")
objeto = Cifrado_Simetrico(mensaje, clave)
resultadoCifrado = objeto.cifrar()
objeto.descifrar(resultadoCifrado) 