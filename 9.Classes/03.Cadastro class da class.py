import os
from dataclasses import dataclass
os.system("clear||cls")

@dataclass
class Endereco:
    logradouro: str
    numero: str

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereco: Endereco

    def exibindo_dados(self):
        print("\nExibindo dados")
        print(f"Nome: {self.nome}, idade: {self.email}, altura: {self.telefone}, Endereço: {self.endereco.logradouro}, numero: {self.endereco.numero}")


nome = input("Digite seu nome: ")
email= input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")

pessoa1 = Pessoa(nome, email, telefone, endereco)
pessoa1.exibindo_dados()






