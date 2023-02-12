# Realice un algoritmo que permita pasar una numero de una base sea cual sea ”M” a 
# otra base “N”, Nota M y N tienen como valor mínimo 2 y como valor máximo 16, 
# además debe pasar el numero a binario y codificar el mensaje en ascii utilizando 
# cifrado cesar en la que el usuario puede seleccionar la dirección y la cantidad de 
# desplazamiento entregar El mensaje ascii sin codificación cesar y con codificación 
# cesar.

def setHexaValue(base):
    hexaValue = {}
    
    if base == 11: hexaValue = { '10': 'A', }
    if base == 12: hexaValue = { '10': 'A', '11': 'B' }
    if base == 13: hexaValue = { '10': 'A', '11': 'B', '12': 'C' }
    if base == 14: hexaValue = { '10': 'A', '11': 'B', '12': 'C', '13': 'D' }
    if base == 15: hexaValue = { '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E' } 
    if base == 16: hexaValue = { '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F' } 
        
    return hexaValue

def getHexaValue(base):

    numberValues = {}
    
    if base == 11: numberValues = { 'A': '10', }
    if base == 12: numberValues = { 'A': '10', 'B': '11', }
    if base == 13: numberValues = { 'A': '10', 'B': '11', 'C': '12', }
    if base == 14: numberValues = { 'A': '10', 'B': '11', 'C': '12', 'D': '13', }
    if base == 15: numberValues = { 'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', } 
    if base == 16: numberValues = { 'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15' } 

    return numberValues

def checkingNumber(number, base):
    value = str(number)
    hexaValue = setHexaValue(base)
    
    if value in hexaValue:
        return hexaValue[value]
    else:
        return value

def checkingHex(value, base):
    value = str(value)
    hexaValue = getHexaValue(base)
    
    if value in hexaValue:
        return hexaValue[value]
    else:
        return value

def decimalToOtherBase(decimal, otherBase):
    number = ""
    
    if decimal <= 0:
        return "0"

    if otherBase > 10:
        while decimal > 0:
            module = int(decimal % otherBase)
            decimal = int(decimal / otherBase)
            number = checkingNumber(module, otherBase) + number
        return number

    while decimal > 0:
        module = int(decimal % otherBase)
        decimal = int(decimal / otherBase)
        number = str(module) + number
    return number

def otherBaseToDecimal(number, base):
    digitsNumber = len(str(number))
    valueInDecimal = 0
    index = 0
    x = - 1

    if base > 10:
        while index < digitsNumber:
            valueExpo = base**index
            valueInDecimal = valueInDecimal + (valueExpo * int(checkingHex(str(number)[x], base)))
            x = x - 1
            index = index + 1
        return valueInDecimal

    try:
        while index < digitsNumber:
            valueExpo = base**index
            valueInDecimal = valueInDecimal + (valueExpo * int(str(number)[x]))
            x = x - 1
            index = index + 1
        return valueInDecimal
    except:
        return "El numero ingresado no corresponde a la base"

def splitBits(binary):
    number = str(binary)
    count = 0
    result = []

    for index in number:
        if ((count % 8) == 0):
            result.append(number[count:(count+8)])
        count+=1

    return result

def formaterBinary(number):
    binary = str(decimalToOtherBase(number, 2))
    lengthBinary = len(binary)

    module = lengthBinary % 8
    addDigits = ''

    if module != 0:
        addCeros = 8 - module
        index = 1
        while True:
            
            if index > addCeros:
                break
            else:
                addDigits = "0" + addDigits
            index = index + 1
    binary = addDigits + binary

    return binary

def decoder(binary):
    numbers = binary
    message = ""
    for numero_binario in numbers:
        numero_decimal = int(numero_binario, 2)
        ASCII = chr(numero_decimal)
        message += ASCII
    return message

def coderCesar(binary, digist):
    numbers = binary
    message = ""
    for numero_binario in numbers:
        numero_decimal = int(numero_binario, 2) + digist

        if numero_decimal>255:
            numero_decimal = 0 + (digist - 1)

        ASCII = chr(numero_decimal)
        message += ASCII
    return message
    

def runCode():
    number = None
    base = None
    otherBase = None
    errorType = None
    valueCesar = None

    while True:
        try:
            print("")
            number = input("Favor digite el numero a comvertir: ")
            base = int(input("Favor digite la base del numero actual: "))
            otherBase = int(input("Favor digite la base a la que desea comvertir el numero anterior: "))
            valueCesar = input("Favor digite el valor con el que desea codigicar en cesar, usando su signo como direccion: ")

            try:
                valueCesar = int(valueCesar)
            except:
                print("")
                print("El valor del codigo cesar debe ser de tipo int")

            if base < 2 or otherBase > 16:
                errorType = 1
                raise Exception("")

            number = number.upper()
            
            valueInDecimal = otherBaseToDecimal(number, base)
            result = decimalToOtherBase(valueInDecimal, otherBase)
            resultFormated = splitBits(formaterBinary(valueInDecimal))
            resultASCII = decoder(resultFormated)
            resultCesar = coderCesar(resultFormated, valueCesar)

            messageInfo = 'El numero => {} de base => {}'.format(number, base)
            messageResult = 'es igual a => {} en base => {}'.format(result, otherBase)
            messageASCII = 'Su valor en ASCII es => {}'.format(resultASCII)
            messageCesar = 'Su valor en ASCII con codificado cesar es => {}'.format(resultCesar)

            print("-----------------------------------------------------")
            print(messageInfo)
            print(messageResult)

            print("")
            print(messageASCII)
            print(messageCesar)

            print("")
            print("Gracias por usar nuestro conversor")
            print('------------------------------------------------------')
            break
        except Exception:
            if errorType == 1:
                print("")
                print("Las base actual y a converit deben ser mayor o iguales a 2 y menor o igual a 16")
runCode()
            
