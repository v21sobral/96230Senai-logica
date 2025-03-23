import os
os.system("cls||clear")

print("""          Restaurante restaurante
      
__________________Cardápio____________________
Código     |       Prato      |         Valor
1          |      Picanha     |       R$ 25,00
2          |      Lasanha     |       R$ 20,00
3          |    Strogonoff    |       R$ 18,00
4          |  Bife Acebolado  |       R$ 15,00
5          |    Pão com ovo   |       R$ 100,00
""")

picanha = "R$ 25,00"
lasanha = "R$ 20,00"
strogonoff = "R$ 18,00"
bife_acebolado = "R$ 15,00"
pao_com_ovo = "R$ 100,00"


codigo = (input("Digite o cógigo da refeição desejada: "))





match codigo:
    case "1":
     print("Voce escolheu: Picanha")
     confirmacodigo =input("Confirmar o pedido?(S/N): ").upper
     while confirmacodigo == "N":
        codigo = (input("Digite o cógigo da refeição desejada: "))
     if confirmacodigo == "S":
        print("Total a pagar:",picanha)
    case "2":
     print("Voce escolheu: Lasanha")
     confirmacodigo =(input("Confirmar o pedido?(S/N): ")).upper
     while confirmacodigo == "N":
        codigo = (input("Digite o cógigo da refeição desejada: "))
     if confirmacodigo == "S":
        print("Total a pagar:",lasanha)
    case "3":
     print("Voce escolheu: Strogonoff")
     confirmacodigo =(input("Confirmar o pedido?(S/N): ")).upper
     while confirmacodigo == "N":
        codigo = (input("Digite o cógigo da refeição desejada: "))
     if confirmacodigo == "S":
        print("Total a pagar:",strogonoff)
    case "4":
     print("Voce escolheu: Bife Acebolado")
     confirmacodigo =(input("Confirmar o pedido?(S/N): ")).upper
     while confirmacodigo == "N":
        codigo = (input("Digite o cógigo da refeição desejada: "))
     if confirmacodigo == "S":
        print("Total a pagar:",bife_acebolado)
    case "5":
     print("Voce escolheu: Pão com ovo")
     confirmacodigo =(input("Confirmar o pedido?(S/N): ")).upper
     while confirmacodigo == "N":
        codigo = (input("Digite o cógigo da refeição desejada: "))
     if confirmacodigo == "S":
        print("Total a pagar:",pao_com_ovo)

      
       
    
  
     

     
    

    