from datetime import datetime

def dias_passados_desde_data(data):
    try:
        data_atual = datetime.now()
        data_fornecida = datetime.strptime(data, "%d/%m/%Y")
        diferenca = data_atual - data_fornecida
        return diferenca.days
    except ValueError:
        return "Data inválida!"

# Exemplo de uso
data_fornecida = input("Digite a data no formato dd/mm/aaaa: ")
dias_passados = dias_passados_desde_data(data_fornecida)
print(f"Já se passaram {dias_passados} dias desde a data fornecida.")

