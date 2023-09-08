def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_obesidade(imc):
    if imc < 18.5:
        return "MAGREZA", 0
    elif imc < 25.0:
        return "NORMAL", 0
    elif imc < 30.0:
        return "SOBREPESO", "I"
    elif imc < 40.0:
        return "OBESIDADE", "II"
    else:
        return "OBESIDADE GRAVE", "III"

# Exemplo de uso
peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

imc = calcular_imc(peso, altura)
classificacao, grau_obesidade = classificar_obesidade(imc)

print("IMC:", imc)
print("Classificação:", classificacao)
print("Obesidade (Grau):", grau_obesidade)
