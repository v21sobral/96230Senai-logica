import os
os.system("cls || clear")


def imc_pesoideal(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return "Abaixo do peso (Consulte a orientação de um nutricionista)"
    elif 18.5 <= imc < 24.9:
        return "Peso normal (Mantenha hábitos saudáveis!)"
    elif 25 <= imc < 29.9:
        return "Sobrepeso (Considere uma dieta balanceada e atividade física)"
    elif 30 <= imc < 34.9:
        return "Obesidade grau 1 (Procure a orientação de um profissional de saúde)"
    elif 35 <= imc < 39.9:
        return "Obesidade grau 2 (Consulte um médico para avaliação e orientação)"
    elif imc >= 40:  
        return "Obesidade grau 3 (Busque assistência médica imediatamente)"
    
      


peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))
imc = peso / (altura ** 2)  
classificacao = imc_pesoideal(peso, altura) 
print(f"Seu IMC é: {imc:.2f}")  # Exibe o valor numérico do IMC
print(f"Classificação: {classificacao}")  # Exibe a classificação
print("\n")
