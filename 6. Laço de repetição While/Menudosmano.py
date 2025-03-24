import os
os.system("cls||clear")


total = 0.0
pedido_valido = False

while True:
    print("Cardápio:")
    print("1 - Picanha - R$25,00")
    print("2 - Lasanha - R$20,00")
    print("3 - Strogonoff - R$18,00")
    print("4 - Bife Acebolado - R$15,00")
    print("5 - Pão com ovo - R$5,00")
    opcao = input("\nEscolha o número do prato desejado: ")
    pedido_valido = False  # Reset the flag at the start of each iteration
    
    if opcao == "1":
        total += 25.00
        print("Picanha adicionada ao pedido!")
        pedido_valido = True
    elif opcao == "2":
        total += 20.00
        print("Lasanha adicionada ao pedido!")
        pedido_valido = True
    elif opcao == "3":
        total += 18.00
        print("Strogonoff adicionado ao pedido!")
        pedido_valido = True
    elif opcao == "4":
        total += 15.00
        print("Bife Acebolado adicionado ao pedido!")
        pedido_valido = True
    elif opcao == "5":
        total += 5.00
        print("Pão com ovo adicionado ao pedido!")
        pedido_valido = True
    else:
        print("Opção inválida! Escolha um número de 1 a 5.")
    
    # Only ask to continue if the order was valid
    if pedido_valido:
        resposta = input("\nDeseja pedir mais alguma coisa? (s/n): ")
        if resposta.lower() != "s":
            break

print(f"\nTotal a pagar: R${total:.2f}")
print("Obrigado pela preferência!")