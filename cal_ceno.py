import math

def calcular_coseno(numero):
    return math.cos(numero)

def calculadora_coseno():
    print("Calculadora de Coseno")
    numero = float(input("Ingrese un número: "))
    resultado = calcular_coseno(numero)
    print(f"El coseno de {numero} es igual a: {resultado}")

if __name__ == "__main__":
    calculadora_coseno()