import os
from dataclasses import dataclass
os.system("clear||cls")

@dataclass
class Endereco:
    logradouro: str
    numero: str
    cidade: str

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: Endereco

    def exibindo_dados(self):
        print("\nExibindo dados")
        print(f"Nome: {self.nome}, email: {self.email}, Endereço: {self.endereco.logradouro}, {self.endereco.numero}, {self.endereco.cidade}")


nome = input("Digite seu nome: ")
email= input("Digite seu email: ")
cidade = input("Digite sua cidade: ")
logradouro = input("Digite seu endereço: ")
numero = input("Digite seu número: ")

endereco1 = Endereco(logradouro, numero,cidade)
pessoa1 = Pessoa(nome, email, endereco1)
pessoa1.exibindo_dados()






