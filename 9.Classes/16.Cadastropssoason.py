import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoas:
    nome: str
    data_de_nascimento: int
    rg: int
    cpf: int

   

lista_de_pessoas = []
QUNTIDADE_DE_PESSOAS = 5

for i in range(QUNTIDADE_DE_PESSOAS):
    pessoas = Pessoas(
                        nome = input("Digite seu nome: "), 
                        data_de_nascimento = int(input("Digite sua idade: ")),
                        rg = int(input("Digite seu RG: ")),
                        cpf = int(input("Digite seu CPF: "))
                        )

    

#Salnvando dados em arquivo txt
nome_arquivo = "Cadastro de pessoas.txt"
with open(nome_arquivo, "a") as cadastro_pessoas:
    for pessaos in lista_de_pessoas:
        cadastro_pessoas.write(f"{pessoas.nome}, {pessoas.data_de_nascimento}, {pessoas.rg}, {pessoas.cpf}\n")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            print(f"{linha.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado.")