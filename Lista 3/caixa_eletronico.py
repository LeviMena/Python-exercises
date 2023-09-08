def calcular_quantidade_cedulas(saque):
    cedulas = [200, 100, 50, 20, 10, 5, 2]
    quantidade_cedulas = []

    for cedula in cedulas:
        quantidade = saque // cedula
        saque %= cedula
        quantidade_cedulas.append(quantidade)

    resultado = ""
    for i in range(len(cedulas)):
        if quantidade_cedulas[i] > 0:
            if resultado:
                resultado += ", "
            resultado += f"{quantidade_cedulas[i]} cédula(s) de {cedulas[i]}"

    return resultado

# Exemplos de uso
saque = int(input("Digite o valor do saque: "))
resultado_saque = calcular_quantidade_cedulas(saque)
print(f"A menor quantidade de cédulas para o saque de R${saque} é: {resultado_saque}")
