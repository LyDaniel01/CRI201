import base64
def ejercicio1():
    pares = [99, 121, 116, 123, 114, 95, 95, 104, 95, 111, 95, 110, 101, 115, 115]
    impares = [114, 112, 111, 111, 100, 121, 99, 114, 115, 110, 105, 118, 114, 111, 125]
    flagASCII = []
    for i in range(15):
        flagASCII.append(pares[i])
        flagASCII.append(impares[i])
    print(flagASCII)
    flag = ""
    for i in range(len(flagASCII)):
        flag += chr(flagASCII[i])
    print(flag)

def ejercicio2():
    cadena = "7d73657665725f6c615f6e61765f73657479625f736f6c7b6f7470797263"
    cadenaBYTES = bytes.fromhex(cadena)
    flag = cadenaBYTES[::-1]
    print(flag)


def ejercicio3():
    cadenaB64 = "Y3J5cHRve2RlX2Jhc2U2NF9hX2hleGFkZWNpbWFsfQ=="
    cadenaBytes = base64.b64decode(cadenaB64)
    cadenaHex = cadenaBytes.hex()
    print(cadenaBytes)
    print(cadenaHex)

def ejercicio4():
    a = "xd"
    print(a)


def ejercicio5():
    a = "XD"
    print(a)

def ejercicio6():
    a = "xd"
    print(a)

def ejercicio7():
    a = "XD"
    print(a)

def ejercicio8():
    a = "xd"
    print(a)

def ejercicio9():
    a = "XD"
    print(a)

def ejercicio10():
    a = "xd"
    print(a)



#ejercicio1()
#ejercicio2()
#ejercicio3()
ejercicio4()
#ejercicio5()
#ejercicio6()
#ejercicio7()
#ejercicio8()
#ejercicio9()
#ejercicio10()