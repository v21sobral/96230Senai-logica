import os
os.system("clear")

nome_empregado = input("Digite deu nome: ")
codigo_empregado = int(input("Digite o número de sua matrícula: " ))
data_nascimento = int(input("Digite seu ano de nascimento: "))
tempo_trabalho = int(input("Digite quantos anos trabalhados: "))
anos_idade = 2025 - data_nascimento


if anos_idade >= 65 and tempo_trabalho >= 30:
    print(f"Senhor(a): {nome_empregado} tem {anos_idade} anos de idade e tem {tempo_trabalho} de anos trabalhados e poderá se aposentar.")
elif anos_idade >= 65:
    print(f"Senhor(a): {nome_empregado} tem {anos_idade} anos de iadade e está apto a se aposentar.")
elif tempo_trabalho >= 30:
    print(f"Senhor(a): {nome_empregado} tem {tempo_trabalho} anos de trabalho e está apto a se aposentar por tempo de trabalho.")
else:
    print(f"Senhor(a): {nome_empregado} Você não está apto a se aposentar")