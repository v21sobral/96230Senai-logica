import os
import time

os.system("cls || clear")

class Endereco:
    def escola(self, logradouro, numero, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"{self.logradouro}, Nº {self.numero}, {self.cidade}/{self.estado}"

class Aluno:
    def escola(self, nome, data_de_nascimento, ra, curso, endereco):
        self.nome = nome
        self.data_de_nascimento = data_de_nascimento
        self.ra = ra
        self.curso = curso
        self.endereco = endereco

    def __str__(self):
        return (f"- Nome: {self.nome}, Data de Nascimento: {self.data_de_nascimento}, "
                f"R.A: {self.ra}, Curso: {self.curso}\n  Endereço: {self.endereco}")

def verificar_lista_vazia(lista_alunos):
    if not lista_alunos:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar_aluno(lista_alunos):
    nome = input("Nome: ").strip()
    data_de_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
    ra = input("R.A: ").strip()
    curso = input("Curso: ").strip()
    logradouro = input("Logradouro: ").strip()
    numero = input("Número: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("Estado: ").strip()
    endereco = Endereco(logradouro, numero, cidade, estado)
    aluno = Aluno(nome, data_de_nascimento, ra, curso, endereco)
    lista_alunos.append(aluno)
    print(f"\n{nome} adicionado com sucesso.")

def mostrar_alunos(lista_alunos):
    if verificar_lista_vazia(lista_alunos):
        return
    print("\n - Lista de alunos - ")
    for a in lista_alunos:
        print(a)

def atualizar_aluno(lista_alunos):
    if verificar_lista_vazia(lista_alunos):
        return
    mostrar_alunos(lista_alunos)
    ra_antigo = input("Digite o R.A do aluno que deseja atualizar: ").strip()
    for aluno in lista_alunos:
        if aluno.ra == ra_antigo:
            aluno.nome = input(f"Novo nome (ou ENTER para manter): ").strip() or aluno.nome
            aluno.data_de_nascimento = input(f"Nova data de nascimento (ou ENTER para manter): ").strip() or aluno.data_de_nascimento
            aluno.ra = input(f"Novo R.A (ou ENTER para manter): ").strip() or aluno.ra
            aluno.curso = input(f"Novo curso (ou ENTER para manter): ").strip() or aluno.curso
            print("\n--- Atualizar Endereço ---")
            aluno.endereco.logradouro = input(f"Novo logradouro (ou ENTER para manter): ").strip() or aluno.endereco.logradouro
            aluno.endereco.numero = input(f"Novo número (ou ENTER para manter): ").strip() or aluno.endereco.numero
            aluno.endereco.cidade = input(f"Nova cidade (ou ENTER para manter): ").strip() or aluno.endereco.cidade
            aluno.endereco.estado = input(f"Novo estado (ou ENTER para manter): ").strip() or aluno.endereco.estado
            print(f"{aluno.nome} foi atualizado.")
            return
    print(f"\nO R.A {ra_antigo} não foi encontrado.")

def excluir_aluno(lista_alunos):
    if verificar_lista_vazia(lista_alunos):
        return
    mostrar_alunos(lista_alunos)
    ra_remover = input("Digite o R.A do aluno que deseja remover: ").strip()
    for aluno in lista_alunos:
        if aluno.ra == ra_remover:
            lista_alunos.remove(aluno)
            print(f"Aluno com R.A {ra_remover} foi removido com sucesso.")
            return
    print(f"O R.A {ra_remover} não foi encontrado.")

alunos = []

while True:
    print("""
    === Bem-vindo ao gerenciador de alunos ===
    1 - Adicionar aluno
    2 - Listar alunos
    3 - Atualizar aluno
    4 - Remover aluno
    5 - Sair
    """)
    try:
        opcao = int(input("Digite uma das opções acima: "))
    except ValueError:
        print("Opção inválida. Digite um número.")
        time.sleep(2)
        os.system("cls || clear")
        continue

    match opcao:
        case 1:
            adicionar_aluno(alunos)
        case 2:
            os.system("cls || clear")
            mostrar_alunos(alunos)
            decisao = input("Digite (s) para voltar ao menu ou (n) para encerrar o programa: ").lower()
            if decisao == "s":
                os.system("cls || clear")
                continue
            else:
                break
        case 3:
            atualizar_aluno(alunos)
        case 4:
            excluir_aluno(alunos)
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