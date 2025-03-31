import os 
os.system("clear")

import time
import os 
os.system("clear")

salario = 0
soma_salarios = 0
total_familias = 0 
numero_filhos = 0 
filhos = 0
maior_salario = 0
menor_salario = 25000000

while True:
    print("""
Código | Descrição 
1 \t Adicionar Pessoa
2 \t Sair e Exibir Resultado

""")
    opcao = int(input("Digite a opção desejada: "))  
    match opcao:
        case 1:
            salario = float(input("Digite o valor do seu sálario: "))
            filhos = int(input("Digite a quantidade de filhos: ")) 
            total_familias += 1
            soma_salarios += salario
            numero_filhos += filhos
            if salario > maior_salario:
                maior_salario = salario
            if salario < menor_salario:
                menor_salario = salario 
        case 2:    
            if total_familias > 0: 
                print(f"\nExibindo resultados")
                print(f"Total de familias: {total_familias}")
                print(f"Média de salários: R$ {soma_salarios / total_familias:.3f}")
                print(f"Média de filhos: {numero_filhos / total_familias:.0f}")
                print(f"Maior salário: {maior_salario:.3f}")
                print(f"Menor salário: {menor_salario:.3f}")
                print(f"\nPrograma encerrado")
            elif total_familias == 0:
                print("\nCadastre uma pessoa primeiro.")
           
            break
        case _:
            print("Opção inválida")
            time.sleep(3)
            os.system("clear")