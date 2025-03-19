import os
os.system("cls||clear")

logincadastrado= "Victor"
senhacadastrada= "123456w"


for i in range(3):
    login= input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    

    if login == logincadastrado and senha== senhacadastrada:
     print("Acesso permitido.\n")
     break
  
    else:
       if i == 2:
        print("Seu login está bloqueado!")
        break

