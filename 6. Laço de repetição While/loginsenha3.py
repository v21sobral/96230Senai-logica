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

    elif login != logincadastrado or senha != senhacadastrada:
      print("Login ou senha incorretos\n")
    
    if i == 2:
       print("Login bloqueado.")
      
    