def calcular_conceito(media):
    if media >= 0.0 and media <= 4.9:
        conceito = "D"
    elif media >= 5.0 and media <= 6.9:
        conceito = "C"
    elif media >= 7.0 and media <= 8.9:
        conceito = "B"
    elif media >= 9.0 and media <= 10.0:
        conceito = "A"
    else:
        return "Média inválida!"

    return f"Conceito: {conceito}"

# Exemplo de uso
media_aluno = float(input("Digite a média do aluno: "))
conceito_aluno = calcular_conceito(media_aluno)
print(conceito_aluno)
