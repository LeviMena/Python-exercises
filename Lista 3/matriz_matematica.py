def ler_matriz():
    matriz = []
    for i in range(1, 4):
        linha = []
        for j in range(1, 4):
            valor = int(input(f"Digite o valor da posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def coluna_maior_valor(matriz):
    maior_valor = float('-inf')
    coluna_maior = None
    soma_valores = 0

    for j in range(1, 4):
        soma_coluna = sum(matriz[i-1][j-1] for i in range(1, 4))
        if soma_coluna > soma_valores:
            soma_valores = soma_coluna
            coluna_maior = j

    return coluna_maior, soma_valores

def linha_menor_valor(matriz):
    menor_valor = float('inf')
    linha_menor = None
    soma_valores = 0

    for i in range(1, 4):
        soma_linha = sum(matriz[i-1])
        if soma_linha < soma_valores:
            soma_valores = soma_linha
            linha_menor = i

    return linha_menor, soma_valores

# Exemplo de uso
matriz = ler_matriz()
coluna, soma_coluna = coluna_maior_valor(matriz)
linha, soma_linha = linha_menor_valor(matriz)

print("Coluna com maior valor:")
print(f"Coluna: {coluna}")
print(f"Soma dos valores: {soma_coluna}")
print()
print("Linha com menor valor:")
print(f"Linha: {linha}")
print(f"Soma dos valores: {soma_linha}")

