import random

# Função para verificar se uma matriz é um quadrado mágico
def verificar_quadrado_magico(matriz):
    # Verificar a soma de referência
    soma_referencia = sum(matriz[0])
# Verificar as somas das linhas
    for linha in matriz:
        if sum(linha) != soma_referencia:
            return False
# Verificar as somas das colunas
    for coluna in range(len(matriz)):
        soma_coluna = sum(matriz[linha][coluna] for linha in range(len(matriz)))
        if soma_coluna != soma_referencia:
            return False
# Verificar a soma da diagonal principal
    soma_diagonal_principal = sum(matriz[i][i] for i in range(len(matriz)))
    if soma_diagonal_principal != soma_referencia:
        return False
# Verificar a soma da diagonal secundária
    soma_diagonal_secundaria = sum(matriz[i][len(matriz) - 1 - i] for i in range(len(matriz)))
    if soma_diagonal_secundaria != soma_referencia:
        return False

    return True
# Definir o tamanho da matriz
tamanho = 3

# Gerar uma matriz quadrada com valores aleatórios
matriz = [[random.randint(1, 9) for _ in range(tamanho)] for _ in range(tamanho)]

# Verificar se a matriz é um quadrado mágico
if verificar_quadrado_magico(matriz):
    print("É uma matriz QUADRADO MÁGICO:")
else:
    print("NÃO é uma matriz QUADRADO MÁGICO:")

# Exibir a matriz
for linha in matriz:
    print(linha)
