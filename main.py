def addmultiplenumbers(numbers):
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    if not numbers:
        return 0
    resultado = numbers[0]
    for num in numbers[1:]:
        resultado *= num
    return resultado

def isiteven(num):
    if isinstance(num, int):
        return num % 2 == 0
    return False

def isitaninteger(num):
    return isinstance(num, int)

def main():
    print("Bienvenido a la super calculadora")
   
if __name__ == "__main__":
    main()

