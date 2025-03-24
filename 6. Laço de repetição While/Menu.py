import os
os.system("cls||clear")

cardapio = {
    1: {"Prato": "Picanha","Valor": 25.00},
    2: {"Prato": "Lasanha","Valor": 20.00},
    3: {"Prato": "Strogonoff","Valor": 18.00},
    4: {"Prato": "Bife Acebolado","Valor": 15.00},
    5: {"Prato": "Pão com ovo", "Valor": 100.00}
}

total_a_pagar = 0.0
while True:
    # Exibir o cardápio
    print("Código |     Prato     | Valor")
    for codigo, detalhes in cardapio.items():
        print(f"  {codigo}.     {detalhes['Prato']}: R$ {detalhes['Valor']:.2f}")

    # Pedir ao usuário para escolher um prato
    codigo = int(input("\nDigite o código do prato desejado: "))

    # Verificar se o código é válido
    if codigo:  # Verifica se a entrada é um número
        if codigo in cardapio:
            prato = cardapio[codigo]["Prato"]
            valor = cardapio[codigo]["Valor"]
            total_a_pagar += valor
            print(f"\nVocê escolheu {prato} por R$ {valor:.2f}")
        else:
            print("Código inválido. Por favor, tente novamente.")
    else:
        print("Entrada inválida. Por favor, digite um número.")

    # Perguntar se o usuário deseja escolher outro prato
    continuar = input("\nDeseja escolher outro prato? (s/n): ").upper()
    if continuar != 'S':
        break

# Mostrar o total a pagar
print(f"\nTotal a pagar: R$ {total_a_pagar:.2f}")