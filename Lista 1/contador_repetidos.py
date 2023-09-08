import random
from collections import Counter
import os
os.system('cls')

def generate_random_vetor(tamanho):
    vetor = []
    for _ in range(tamanho):
        vetor.append(random.randint(1, 10))
    return vetor

random_vetor = generate_random_vetor(10)
print("Vetor aleatório:", random_vetor)

counter = Counter(random_vetor)
valores_repetidos = [valor for valor, count in counter.items() if count > 1]

if valores_repetidos:
    print("Valores repetidos encontrados:", valores_repetidos)
    print("Total de valores repetidos:", len(valores_repetidos))
else:
    print("Não foram encontrados valores repetidos no vetor.")