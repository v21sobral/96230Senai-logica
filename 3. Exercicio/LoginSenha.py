import os
os.system("clear")

entrar_usuario = input("Digite seu login: ")
entrar_senha = input("Digite sua senha: ")
entrar_cadastrado = "Victor"
senha_cadastrado = "123456"


if entrar_usuario == entrar_cadastrado and entrar_senha == senha_cadastrado:
    print("BEm-Vindo")
else:
    print("Login ou senha errados")

