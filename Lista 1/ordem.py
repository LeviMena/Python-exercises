import random
import os

os.system('cls') 

vetor = [random.randint(0, 100) for i in range(10)]
print(f'Vetor original: {vetor}')

vetor.sort()
print(f'Vetor ordenado de forma crescente: {vetor}')

vetor.sort(reverse=True)
print(f'Vetor ordenado de forma decrescente: {vetor}')