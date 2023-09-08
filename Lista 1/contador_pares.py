import os
import random
os.system('cls')

vector = [random.randint(1, 100) for _ in range(10)]
print(f"Vetor: {vector}")

even_count = len([x for x in vector if x % 2 == 0])
odd_count = len(vector) - even_count

print(f"Números pares no vetor: {even_count}")
print(f"Números ímpares no vetor: {odd_count}")