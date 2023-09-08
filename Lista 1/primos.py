import os
import random

os.system('cls') 

def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

vetor = [random.randint(1, 100) for _ in range(10)]
print(f"Vetor: {vetor}")

primos = [x for x in vetor if eh_primo(x)]
print(f"Números primos no vetor: {primos}")