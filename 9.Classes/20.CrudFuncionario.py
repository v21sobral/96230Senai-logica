import os
import time

os.system("cls || clear")

# Função para verificar se a lista está vazia.
def verificar_lista_vazia(lista_funcionarios):
    if not lista_funcionarios:
        print("\nA lista está vazia.")
        return True
    return False

# Função para adicionar.
def adicionar_funcionario(lista_funcionarios):
    nome = input("Nome: ").lower()
    data_de_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("CPF: ")
    funcao = input("Função: ").lower()
    funcionario = {
        "nome": nome,
        "data_de_nascimento": data_de_nascimento,
        "cpf": cpf,
        "funcao": funcao
    }
    lista_funcionarios.append(funcionario)
    print(f"\n{nome} adicionado com sucesso.")

# Função para mostrar todos os funcionários.
def mostrar_funcionarios(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        return
    print("\n - Lista de funcionários - ")
    for f in lista_funcionarios:
        print(f"- Nome: {f['nome']}, Data de Nascimento: {f['data_de_nascimento']}, CPF: {f['cpf']}, Função: {f['funcao']}")

# Função para atualizar.
def atualizar_funcionario(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        return
    mostrar_funcionarios(lista_funcionarios)
    nome_antigo = input("Digite o nome do funcionário que deseja atualizar: ").lower()
    for funcionario in lista_funcionarios:
        if funcionario["nome"] == nome_antigo:
            funcionario["nome"] = input(f"Novo nome para {nome_antigo} (ou ENTER para manter): ").lower() or funcionario["nome"]
            funcionario["data_de_nascimento"] = input(f"Nova data de nascimento (ou ENTER para manter): ") or funcionario["data_de_nascimento"]
            funcionario["cpf"] = input(f"Novo CPF (ou ENTER para manter): ") or funcionario["cpf"]
            funcionario["funcao"] = input(f"Nova função (ou ENTER para manter): ").lower() or funcionario["funcao"]
            print(f"{nome_antigo} foi atualizado.")
            return
    print(f"\nO nome {nome_antigo} não foi encontrado.")

# Função para excluir.
def excluir_funcionario(lista_funcionarios):
    if verificar_lista_vazia(lista_funcionarios):
        return
    mostrar_funcionarios(lista_funcionarios)
    nome_remover = input("Digite o nome do funcionário que deseja remover: ").lower()
    for funcionario in lista_funcionarios:
        if funcionario["nome"] == nome_remover:
            lista_funcionarios.remove(funcionario)
            print(f"{nome_remover} foi removido com sucesso.")
            return
    print(f"O nome {nome_remover} não foi encontrado.")

# Lista de funcionários.
funcionarios = []

# Mostrando menu.
while True:
    print("""
    ===Bem vindo ao gerenciador de funcionários===
    1 - Adicionar funcionário
    2 - Listar funcionários
    3 - Atualizar funcionário
    4 - Remover funcionário
    5 - Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_funcionario(funcionarios)
        case 2:
            os.system("cls || clear")
            mostrar_funcionarios(funcionarios)
            decisao = input("Digite (s) para voltar ao menu ou (n) para encerrar o programa: ").lower()
            if decisao == "s":
                os.system("cls || clear")
                continue
            else:
                break
        case 3:
            atualizar_funcionario(funcionarios)
        case 4:
            excluir_funcionario(funcionarios)
        case 5:
            print("\nPrograma sendo encerrado", end="", flush=True)
            for _ in range(3):
                print(".", end="", flush=True)
                time.sleep(1)
            os.system("cls || clear")
            break
        case _:
            print("\nOpção inválida.\nTente novamente.")
    if opcao != 1:
        time.sleep(2)
    os.system("cls || clear")