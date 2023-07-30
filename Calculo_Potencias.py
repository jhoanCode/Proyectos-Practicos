def potencia(base, exponente):
    return base ** exponente

def calculadora_potencias():
    print("Calculadora de Potenciaciones")
    base = float(input("Ingrese el número base: "))
    exponente = float(input("Ingrese el exponente: "))
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la {exponente} es igual a: {resultado}")

if __name__ == "__main__":
    calculadora_potencias()