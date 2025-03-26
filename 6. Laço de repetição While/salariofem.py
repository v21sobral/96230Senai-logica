total_pessoas = 0
soma_salarios = 0
maior_idade = 0
menor_idade = 150  # Valor inicial alto
mulheres_5000 = 0

print("Sistema de Pesquisa de Habitantes")

while True:
    print("\nMenu:")
    print("1 - Cadastrar pessoa")
    print("2 - Ver estatísticas")
    print("3 - Sair")
   
    opcao = input("Escolha uma opção: ")
   
    # Usando match case para o menu
    match opcao:
        case "1":
            print("\nNovo cadastro:")
           
            # Entrada de dados com validação simples
            idade = int(input("Idade: "))
            while idade < 0 or idade > 120:
                print("Idade inválida! Digite entre 0 e 120 anos.")
                idade = int(input("Idade: "))
           
            sexo = input("Sexo (M/F): ").upper()
            while sexo != "M" and sexo != "F":
                print("Opção inválida! Use M ou F.")
                sexo = input("Sexo (M/F): ").upper()
           
            salario = float(input("Salário R$: "))
            while salario < 0:
                print("Salário não pode ser negativo!")
                salario = float(input("Salário R$: "))
           
            # Atualizando estatísticas
            total_pessoas += 1
            soma_salarios += salario
           
            # Usando if para verificar maior/menor idade
            if total_pessoas == 1:
                maior_idade = menor_idade = idade
            else:
                if idade > maior_idade:
                    maior_idade = idade
                if idade < menor_idade:
                    menor_idade = idade
           
            # Verificando mulheres com salário alto
            if sexo == "F" and salario >= 5000:
                mulheres_5000 += 1
           
            print("Cadastro realizado!")
       
        case "2":
            if total_pessoas == 0:
                print("\nNenhum dado cadastrado ainda!")
            else:
                print("\nEstatísticas:")
                print(f"Total de pessoas: {total_pessoas}")
                print(f"Média salarial: R$ {soma_salarios/total_pessoas:.2f}")
                print(f"Maior idade: {maior_idade} anos")
                print(f"Menor idade: {menor_idade} anos")
                print(f"Mulheres com salário ≥ R$5000: {mulheres_5000}")
       
        case "3":
            print("Encerrando o programa...")
            break
       
        case _:
            print("Opção inválida! Tente novamente.")