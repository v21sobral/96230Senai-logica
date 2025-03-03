import os
os.system("clear")

produto = float(input("Digite o valor do produto: "))
pagamento = float(input("""
Formas de pagamento
1 - Pagamento à vista   2 - Pagamento à prazo

Digite o código do pagamento: """))

match pagamento:
    case 1:
        desconto = produto * 0.1
        produto_debito = produto - desconto
        print(f"Valor de {produto:.2f} pago à vista com desconto de 10%: R$ {produto_debito:.2f}")
    case 2:
        parcelamento = int(input("\nDigite o número de parcelas até 6x: "))
        while parcelamento > 6 or parcelamento < 1:
            print("Operação inválida!")
            parcelamento = int(input("\nDigite o número de parcelas até 6x: "))
        parcela = produto / parcelamento    
        print(f"O valor de {produto} em {parcelamento}x ficará em parcelas mensais de: R$ {parcela:.2f}")

                    
        
    case _:
        print("Opção inválida!")

            
        
