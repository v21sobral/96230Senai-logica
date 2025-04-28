import os
os.system("cls || clear")
import time



lista_cadastro = []


def cadastrar_usuario():
    while True:
        print("=== Rede antissocial ===")
        print("Faça seu cadastro para acessar a rede antissocial!")
        cadastro_login = input("Cadastre seu login: ")
        cadastro_senha = input("Cadastre sua senha: ")
        
  
        lista_cadastro.append({"login": cadastro_login, "senha": cadastro_senha})
        
        
        continuar = input("Deseja cadastrar outro usuário? (s/n): ").lower()
        if continuar != 's':
            break
        os.system("cls || clear")
    os.system("cls || clear")

def login_func():
    while True:
        # Solicita login e senha do usuário
        print("\n=== Rede Antissocial ===")
        login_tentativa = input("\nDigite seu login: ")
        senha_tentativa = input("Digite sua senha: ")
        
        # Verifica se o login e senha correspondem a algum usuário cadastrado
        for usuario in lista_cadastro:
            if usuario["login"] == login_tentativa and usuario["senha"] == senha_tentativa:
                print("Login bem-sucedido!")
                print(f"Bem-vindo(a), {login_tentativa} a sua rede antissocial!")
                  # Sai do programa após login bem-sucedido
            else:
                print("Login ou senha incorretos. Tente novamente.")
                time.sleep(1)
                os.system("cls || clear")  # Limpa a tela após erro
                continue

                 

cadastrar_usuario()
login_func()

