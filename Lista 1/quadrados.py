import os

os.system('cls')    

primeiro_vetor = [x**2 for x in range(2, 21) if x % 2 == 0]

segundo_vetor = list(range(10, 20))

soma_vetores = [x + y for x, y in zip(primeiro_vetor, segundo_vetor)]

print(soma_vetores)