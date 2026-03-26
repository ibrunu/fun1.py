def media(a, b, c):
    resultado = (a + b + c) / 3
    return resultado

def main():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))
    
    print("Média:", media(n1, n2, n3))

if __name__ == "__main__":
    main()