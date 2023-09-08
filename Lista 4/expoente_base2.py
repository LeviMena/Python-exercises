def calcular_exponencial(n):
    if n == 0:
        return 1
    else:
        return 2 * calcular_exponencial(n - 1)

# Exemplo de uso
n = int(input("Digite um valor para n: "))
resultado = calcular_exponencial(n)
print("2 elevado a", n, "é igual a", resultado)
