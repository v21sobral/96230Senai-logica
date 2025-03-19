import os
os.system("cls||clear")

login= "Victor"
senha = "123456w"


while True:
    login= input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    

    if login != 'Victor' and senha!= '123456w':
     print("Login ou senha inválidos.\n")
  
    else:
       break

print("Você está logado")