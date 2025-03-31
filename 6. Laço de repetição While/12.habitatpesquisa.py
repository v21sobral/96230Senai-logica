import os
os.system("cls||clear")

import os 
os.system("clear")
import time
idade = 0
quantidade_mulheres = 0 
soma_salarios = 0
total_pessoas = 0
maior_idade = 0
menor_idade = 120



while True:
    print("""
Código | Descrição 
1 \t Adicionar Pessoa
2 \t Exibir Resultado
3 \t Sair
""")
    opcao = int(input("Digite a opção desejada: "))                   
    
    match opcao:
        case 1:
        
            idade = int(input("Digite sua idade: "))
            genero = (input("""                 
M - Masculino
F - Feminino
Digite seu gênero:                    
""")).upper()
            salario = float(input("Digite o valor do seu sálario: "))
            total_pessoas += 1
            soma_salarios += salario
            if genero == "F" and salario >= 5.000:
                quantidade_mulheres += 1
            if idade > maior_idade:
                maior_idade = idade

            if idade < menor_idade:
                menor_idade = idade   
            os.system("clear")    
        case 2:
            if total_pessoas > 0:
               
                print(f"\nMédia salarial do grupo: R$ {soma_salarios / total_pessoas:.3f}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salário a partir de R$ 5.000,00: {quantidade_mulheres}")
            elif total_pessoas == 0:
                print("\nCadastre uma pessoa primeiro.")
            time.sleep(3)  
            os.system("clear")
        case 3:
            print("Encerrando o programa")
            break          
        case _:
            print("\nOpção inválida")
            time.sleep(3)
            os.system("clear")