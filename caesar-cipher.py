#una funcion recibe parametros o variables para realizar una tarea especifica
#cramos una funcion llamada suma
def suma(numero1, numero2):
    resultado= numero1 + numero2
    #devolvemos el valor del proceso
    return resultado
#creamos una variable a con lo que diga el usuario
a = input("escribe un nuemero: ")
#parseamos la cadea que introduzca el usuario
a = int(a)

#pedimos el segundo valor
b= input("ingrese el segundo numero: ")
b= int(b)

#llamamos la funcion para optener el resultado
print(suma(a,b))

#------------------laboratorio 13 ------------------
# La idea es “mover” cada letra del mensaje un número de posiciones (la clave).
# Por ejemplo, si la clave es 3: A -> D, B -> E, C -> F, etc.
# Esta función recibe un alfabeto (un texto) y lo pega consigo mismo.
# Lo hacemos para poder “movernos” hacia adelante sin quedarnos sin letras.
# Ejemplo: "ABC" se vuelve "ABCABC".
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet

# Esta función le pide al usuario que escriba un mensaje.
# Lo que el usuario escriba se guarda y luego se devuelve.
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
# Esta función le pide al usuario una clave.
# La clave es un número del 1 al 25 que indica cuánto se moverán las letras.
def getCipherKey():
    shiftAmount = input("Please enter a key (whole number from 1-25): ")
    return shiftAmount
# Esta función hace el trabajo de encriptar.
# Recorre el mensaje letra por letra, busca cada letra en el alfabeto,
# le suma la clave para “moverla”, y va armando el mensaje encriptado.
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    # Duplico el alfabeto para poder desplazar letras sin problemas
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    # Pido el mensaje al usuario
    myMessage = getMessage()
    print(myMessage)
    # Pido la clave al usuario
    myCipherKey = getCipherKey()
    print(myCipherKey)
    # Encripto el mensaje
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    # Desencripto el mensaje (para comprobar que vuelve al original)
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')

#funcion desencriptar
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    # Aquí reviso cada letra del mensaje (ya en mayúsculas)
    for currentCharacter in uppercaseMessage:
        # Busco en qué posición está la letra dentro del alfabeto
        position = alphabet.find(currentCharacter)
        # Calculo la nueva posición sumando la clave
        newPosition = position + int(cipherKey)
        # Si la letra sí está en el alfabeto, cambio por la letra “movida”
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition] 
        else:
            # Si no es letra (por ejemplo espacio, número o símbolo), la dejo igual
            encryptedMessage = encryptedMessage + currentCharacter
    # Al final devuelvo el texto encriptado completo
    return encryptedMessage
#FUNCION desencriptar
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
#---------llamadas a la funcion runCaesarCipherProgram() -----------
runCaesarCipherProgram()