
def checHexiValue(number):
    number = str(number)

    values = {
        'A': '10',
        'B': '11',
        'C': '12',
        'D': '13',
        'E': '14',
        'F': '15'
    }

    if number in values:
        return values[number]
    else:
        return number

def chekBase(number, base):
    number = str(number)

    for value in number:
        newValue = checHexiValue(value)
        
        if int(newValue) >= int(base):
            print("El valor {} no corresponde a la base {}".format(value, base))
            return

        print("Todo correcto")

chekBase('ABCDE', 15)