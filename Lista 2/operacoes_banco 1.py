# Criação da matriz vazia 5x5
matriz = [[''] * 5 for _ in range(5)]

# Entrada de dados dos clientes
for i in range(5):
    print(f"Informações do cliente {i+1}:")
    numero_conta = input("Número da conta: ")
    nome = input("Nome: ")
    saldo = float(input("Saldo: "))
    op = input("OP (C ou D): ")

    # Armazenando os dados na matriz
    matriz[i][0] = numero_conta
    matriz[i][1] = nome
    matriz[i][2] = saldo
    matriz[i][3] = op

# Exibindo a matriz com o movimento bancário de cada cliente
print("\nMovimento bancário dos clientes:")
for linha in matriz:
    print(linha)

