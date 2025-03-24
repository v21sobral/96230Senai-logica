import os
os.system("cls||clear")
contador = 0
nota1 = 0
print("Calculadora de média\n")

while True:
 contador += 1
 nota1 += int(input("Digite sua nota: "))
 
 confirmar = input("Deseja adicionar outra nota(s/n)?: ")
 if confirmar == "n":
  print(f"Sua média  é : {nota1/contador}")
  break
 else:
  print("opção inválida.")







  
  
  
 