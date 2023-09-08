# Criação da matriz 12x7
matriz = [[''] * 7 for _ in range(12)]

# Entrada de dados dos times
for i in range(12):
    print(f"Informações do time {i+1}:")
    posicao = int(input("Posição: "))
    time = input("Time: ")
    pontos = int(input("Pontos: "))
    jogos = int(input("Jogos: "))
    vitorias = int(input("Vitórias: "))
    empates = int(input("Empates: "))
    derrotas = int(input("Derrotas: "))

    # Armazenando os dados na matriz
    matriz[i][0] = posicao
    matriz[i][1] = time
    matriz[i][2] = pontos
    matriz[i][3] = jogos
    matriz[i][4] = vitorias
    matriz[i][5] = empates
    matriz[i][6] = derrotas

# Ordenar a matriz por pontos (coluna 2) em ordem decrescente
matriz.sort(key=lambda x: x[2], reverse=True)

# a) Campeão brasileiro
campeao = matriz[0][1]

# b) 5 primeiros colocados para a Libertadores da América
classificados_libertadores = [time[1] for time in matriz[:5]]

# c) 5 seguintes (6 a 10) classificados para Copa Sul-Americana
classificados_sulamericana = [time[1] for time in matriz[5:10]]

# d) 2 últimos rebaixados para a Série B
rebaixados = [time[1] for time in matriz[-2:]]

# Exibindo a matriz com o resultado do campeonato
print("\nResultado do Campeonato Brasileiro:")
for linha in matriz:
    print(linha)

# Exibindo os resultados adicionais
print("\nCampeão Brasileiro:", campeao)
print("Classificados para a Libertadores da América:", classificados_libertadores)
print("Classificados para a Copa Sul-Americana:", classificados_sulamericana)
print("Rebaixados para a Série B:", rebaixados)
