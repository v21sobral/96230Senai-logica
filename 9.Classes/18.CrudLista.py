import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    data_de_admissao: int
    matricula: int
    endereco: str

@dataclass
class Cliente:
    nome: str
    data_de_nascimento: int
    endereco: str

   

lista_nomes = []

def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        return True
    return False

def adicionar_nome(lista_nomes):
    nome = input("Digite seu nome: ")
    lista_nomes.append(nome)
    print(f"\n{nome} adcionado com sucesso")


