import base64

def ejercicio1():
    vector = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
    cadena = ""
    for elemento in vector: 
        cadena += chr(elemento)
    print(cadena)

def ejercicio2():
    cadena =  "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
    print(bytes.fromhex(cadena).decode("utf=8"))
    
def ejercicio3():
    cadena = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    cadenaBytes = bytes.fromhex(cadena)
    cadenaB64 = base64.b64encode(cadenaBytes)
    print(cadenaB64.decode("utf=8"))






ejercicio1()
ejercicio2()
ejercicio3()