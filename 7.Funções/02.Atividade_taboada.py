import os
os.system("cls || clear")


def tabuada(numero):
     for t in range(11):
          print(f"{numero} x {t} = {numero * t}")
      
print(":::::Tabuada:::::")
numero = int(input("Digite um número para saber sua tabuada: "))
tabuada(numero)



