def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

def calculadora():
    print("Calculadora básica")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    while True:
        opcion = int(input("Seleccione una operación (1/2/3/4/5): "))

        if opcion == 1:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = suma(num1, num2)
            print("Resultado:", resultado)
        elif opcion == 2:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = resta(num1, num2)
            print("Resultado:", resultado)
        elif opcion == 3:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = multiplicacion(num1, num2)
            print("Resultado:", resultado)
        elif opcion == 4:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = division(num1, num2)
            print("Resultado:", resultado)
        elif opcion == 5:
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    calculadora()
