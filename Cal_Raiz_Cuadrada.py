import math

def suma_raiz_cuadrada(num1, num2):
    return math.sqrt(num1) + math.sqrt(num2)

def calculadora_suma_raiz_cuadrada():
    print("Calculadora de Suma de Raíces Cuadradas")
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = suma_raiz_cuadrada(num1, num2)
    print(f"La suma de las raíces cuadradas de {num1} y {num2} es igual a: {resultado}")

if __name__ == "__main__":
    calculadora_suma_raiz_cuadrada()
