def ler_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Digite o valor da posição [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def soma_diagonais(matriz):
    soma_principal = 0
    soma_secundaria = 0

    for i in range(3):
        soma_principal += matriz[i][i]
        soma_secundaria += matriz[i][2 - i]

    return soma_principal, soma_secundaria

# Exemplo de uso
matriz = ler_matriz()
soma_principal, soma_secundaria = soma_diagonais(matriz)

print("Soma da diagonal principal:", soma_principal)
print("Soma da diagonal secundária:", soma_secundaria)

