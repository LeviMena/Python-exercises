def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def serie_fibonacci(n):
    for i in range(n):
        print(fibonacci(i), end=' ')

# Exemplo de uso
serie_fibonacci(12)
