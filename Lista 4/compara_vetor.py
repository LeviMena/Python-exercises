import random

def gerar_vetor():
    vetor = []
    for _ in range(10):
        valor = random.randint(1, 100)
        vetor.append(valor)
    return vetor

def encontrar_maior(vetor):
    if len(vetor) == 1:
        return vetor[0]
    else:
        sub_vetor = vetor[1:]
        maior_sub_vetor = encontrar_maior(sub_vetor)
        return max(vetor[0], maior_sub_vetor)

# Exemplo de uso
vetor = gerar_vetor()
print("Vetor:", vetor)

maior_valor = encontrar_maior(vetor)
print("Maior valor:", maior_valor)
