import os
os.system("cls||clear")



print("Bem-vindo ao sistema de cálculo de média!")

# Solicita as três notas, garantindo que estejam entre 0 e 10
while True:
    nota1 = float(input("Digite a primeira nota: "))
    if nota1:  # Verifica se é um número válido
        
        if 0 <= nota1 <= 10:
            break
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10.")
    else:
        print("Entrada inválida! Por favor, insira um número.")

while True:
    nota2 = float(input("Digite a segunda nota: "))
    if nota2:  # Verifica se é um número válido
        if 0 <= nota2 <= 10:
            break
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10.")
    else:
        print("Entrada inválida! Por favor, insira um número.")

while True:
    nota3 = float(input("Digite a terceira nota: "))
    if nota3:  # Verifica se é um número válido

        if 0 <= nota3 <= 10:
            break
        else:
            print("Nota inválida! A nota deve estar entre 0 e 10.")
    else:
        print("Entrada inválida! Por favor, insira um número.")

# Calcula a média
media = (nota1 + nota2 + nota3) / 3

# Verifica a situação do aluno
if media >= 7:
    situacao = "Aprovado"
elif 5 <= media < 7:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Exibe o resultado
print(f"\nMédia do aluno: {media:.2f}")
print(f"Situação: {situacao}")