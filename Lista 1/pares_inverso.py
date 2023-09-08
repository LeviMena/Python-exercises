import os
os.system('cls')

vector = list(range(10, 21))
print(f"Vetor: {vector}")

even_numbers = [x for x in vector if x % 2 == 0]
even_numbers.reverse()
print(f"Números pares do vetor de trás para frente: {even_numbers}")