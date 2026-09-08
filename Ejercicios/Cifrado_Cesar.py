class CifradoCesar:
    # Definicion del constructor
    def __init__(self):
        # 26 caracteres
        # indices 0 - 25
        self.vector = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def getVector(self):
        return self.vector

    def encriptarMensaje(self, mensaje, desplazamiento):
        cadenaEncriptada = ""
        for letra in mensaje:
            for alfabeto in self.getVector():
                if letra.upper() == alfabeto:
                    indice = self.getVector().index(letra.upper())
                    posicion = indice + desplazamiento
                    if posicion >= 26:
                        posicion = posicion % 26
                    cadenaEncriptada += self.getVector()[posicion]
            if letra == " ":
                cadenaEncriptada += " "
        print(cadenaEncriptada)

objeto = CifradoCesar()
objeto.encriptarMensaje("HOLA ESTE ES UN MENSAJE CIFRADO DESDE LA ASIGNATURA CRIPTOGRAFIA I",800)
