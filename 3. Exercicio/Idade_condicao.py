import os
os.system("clear")


numero = int(input("Digite um numero para saber se é maior que 10: "))

while numero < 18:
    if numero < 10:
       print("Esse número é maior que 10")
       print("Aprendeu cabeção!?")
       print("________________________________________________________ ")
       print("Digite um número maior que 10 para encerrar o programa.")
    elif numero == 10:
       print("Você escolheu 10, tá querendo tirar com minha cara? ¬¬")
       print("________________________________________________________ ")
       print("Digite um número maior que 10 para encerrar o programa.")
    else: 
       print("Esse número é amior que 10")
       print("Aprendeu cabeção!?")
       print("________________________________________________________ ")
       print("Digite um número maior que 10 para encerrar o programa.")
    
    print("")
    numero = int(input("Digite um numero para saber se é maior que 10: "))

else:
    print("Programa encerrado")






