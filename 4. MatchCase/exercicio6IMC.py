import os
os.system("clear")

print("Calcule seu Índice de Massa Corpóreo")
nome_usuario = str(input("\nDigite seu nome: "))
peso_usuario = float(input("Digite seu peso: "))
genero_usuario = input("""Digite para masculino       Digite para feminino
         M                             F
Digite seu sexo: """)


match genero_usuario:
    case 1:
        

