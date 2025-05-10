import os
import time

os.system("cls || clear")

# Função para verificar se a lista está vazia.
def verificar_lista_vazia(lista_nomes):
    if not lista_nomes: # Se a lista NÃO tem conteúdo, retona o valor 'VERDADEIRO'
        print("\nA lista está vazia.")
        return True
    return False # Se a lista possui algum conteúdo.


# Função para adicionar.
def adicionar_nome(lista_nomes):
    nome = input("Digite o nome que deseja adicionar: ").lower()
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso.")


# Função para mostar todos os nomes da lista.
def mostrar_nomes(lista_nomes):
    # Vefificar se a lista está vazia.
    if verificar_lista_vazia(lista_nomes):
        return

    print("\n - Lista de nomes - ")
    for nome in lista_nomes:
        print(f"- {nome}")


# Função para atualizar.
def atualizar_nome(lista_nomes):
    # Verificar se a lista está vazia.
    if verificar_lista_vazia(lista_nomes):
        return

    mostrar_nomes(lista_nomes)
    nome_antigo = input("Digite o nome que deseja atualizar: ").lower()
    if nome_antigo in lista_nomes: # Percorre a lista para encontrar o nome informado.
        novo_nome = input(f"Digite o novo nome para {nome_antigo}: ").lower()
        indice = lista_nomes.index(nome_antigo) # Encontra a posicão (índice) do nome dentro da lista.
        lista_nomes[indice] = novo_nome # Substitui o conteúdo anterior pelo novo nome.
        print(f"{nome_antigo} foi atualizado para {novo_nome}.")
    else:
        print(f"\nO nome {nome_antigo} não foi encontrado.")


# Função para excluir.
def excluir_nome(lista_nomes):
    # Verificar se a lista está vazia.
    if verificar_lista_vazia(lista_nomes):
        return

    # Mostra lista de usuários
    mostrar_nomes(lista_nomes)

    nome_remover = input("Digite o nome que deseja remover: ").lower()
    if nome_remover in lista_nomes: # Percorre a lista para encontrar o nome informado.
        lista_nomes.remove(nome_remover) # Remove o nome informado.
        print(f"{nome_remover} foi removido com sucesso.")
    else:
        print(f"O nome {nome_remover} não foi encontrado.")


# Criadno lista de nomes.
nomes = []

# Mostrando menu.
while True:
    print("""
    ===Bem vindo ao gerenciador de nomes===
    1 - Adicionar
    2 - Listar nomes
    3 - Atualizar
    4 - Remover
    5 - Sair
    """)
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            adicionar_nome(nomes)
        case 2:
            if opcao == 2:
                os.system("cls || clear")
                mostrar_nomes(nomes)
                decisao = input("Digite (s) para voltar ao menu ou (n) para encerrar o programa: ").lower()
                if decisao == "s":
                    os.system("cls || clear")
                    continue
                else:
                    break
        case 3:
            atualizar_nome(nomes)
        case 4:
            excluir_nome(nomes)
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