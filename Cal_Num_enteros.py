def suma_enteros(num1, num2):
    return num1 + num2

def calculadora_suma_enteros():
    print("Calculadora de Suma de Números Enteros")
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))
    resultado = suma_enteros(num1, num2)
    print(f"La suma de {num1} y {num2} es igual a: {resultado}")

if __name__ == "__main__":
    calculadora_suma_enteros()