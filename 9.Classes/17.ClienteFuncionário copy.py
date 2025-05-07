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

   

lista_de_funcionarios= []
lista_de_clientes = []
QUNTIDADE_DE_PESSOAS = 3

opcao = input("Digite 1 para cadastrar funcionário e 2 para cadastrar o cliente: ")
match opcao:
    case '1':
        for i in range(QUNTIDADE_DE_PESSOAS):
            print("===Cadastre o funcionário===")
            funcionario = Funcionario(
                                nome = input("Digite seu nome: "), 
                                data_de_admissao = int(input("Digite sua idade: ")),
                                matricula = int(input("Digite seu RG: ")),
                                endereco = input("Digite seu CPF: ")
                                )
            lista_de_funcionarios.append(funcionario)
            print(" ")
        nome_arquivo = "Cadastro de funcionarios.txt"
        with open(nome_arquivo, "a") as cadastro_funcionarios:
            for funcionario in lista_de_funcionarios:
                cadastro_funcionarios.write(f"{funcionario.nome}, {funcionario.data_de_admissao}, {funcionario.matricula}, {funcionario.endereco}\n")
    case '2':
        for i in range(QUNTIDADE_DE_PESSOAS):
            print("===Cadastre o cliente===")
            cliente = Cliente(
                                nome = input("Digite seu nome: "), 
                                data_de_nascimento = int(input("Digite sua idade: ")),
                                endereco = input("Digite seu CPF: ")
                                )
            lista_de_clientes.append(cliente)
            print(" ")
        nome_arquivo = "Cadastro de clientes.txt"
        with open(nome_arquivo, "a") as cadastro_clientes:
            for cliente in lista_de_clientes:
                cadastro_clientes.write(f"{cliente.nome}, {cliente.data_de_nascimento}, {cliente.endereco}\n")

    case _:
        print("Apenas opções 1 ou 2.")

    

#Salnvando dados em arquivo txt


