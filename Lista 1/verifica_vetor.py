import os
import random
os.system('cls')

def gera_vetor_aleatorio(tamanho):
    vetor = []
    for _ in range(tamanho):
        vetor.append(random.randint(1, 100))
    return vetor

def encontrar_valor(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i + 1
    return -1

# Criação do vetor aleatório
random_vetor = gera_vetor_aleatorio(10)
print("Vetor aleatório:", random_vetor)

# Leitura do valor
valor = int(input("Digite um valor para verificar no vetor: "))

# Verificação
posicao = encontrar_valor(random_vetor, valor)
if posicao != -1:
    print("O valor", valor, "foi encontrado na posição", posicao)
else:
    print("O valor", valor, "não foi encontrado no vetor.")