import os
os.system("clear")

produto = float(input("Digite o valor do produto: "))
pagamento = int(input("""
Código \t Forma de pagamento
1 -\t Pagamento à vista
2 -\t Pagamento à prazo

Digite o código do pagamento: 
"""))

match pagamento:
    case 1:
        desconto = produto * 0.1
    case 2:
        parcela = int(input("Digite o número de parcelas até 6x: "))
        
