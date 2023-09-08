# Criação da matriz vazia 4x4
matriz = [[''] * 4 for _ in range(4)]

# Entrada de dados dos funcionários
for i in range(4):
    print(f"Informações do funcionário {i+1}:")
    matricula = input("Matrícula: ")
    nome = input("Nome: ")
    funcao = input("Função: ")
    salario = float(input("Salário: "))

    # Armazenando os dados na matriz
    matriz[i][0] = matricula
    matriz[i][1] = nome
    matriz[i][2] = funcao
    matriz[i][3] = salario

# Encontrando o funcionário com o maior e o menor salário
maior_salario = matriz[0][3]
menor_salario = matriz[0][3]
funcionario_maior_salario = matriz[0][1]
funcionario_menor_salario = matriz[0][1]

for i in range(1, 4):
    salario = matriz[i][3]
    if salario > maior_salario:
        maior_salario = salario
        funcionario_maior_salario = matriz[i][1]
    elif salario < menor_salario:
        menor_salario = salario
        funcionario_menor_salario = matriz[i][1]

# Exibindo a matriz com a folha de pagamento da empresa
print("\nFolha de pagamento da empresa:")
for linha in matriz:
    print(linha)

# Exibindo o funcionário com o maior e o menor salário
print("\nFuncionário com maior salário:", funcionario_maior_salario)
print("Funcionário com menor salário:", funcionario_menor_salario)
