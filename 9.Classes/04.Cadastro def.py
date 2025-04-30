import os
from dataclasses import dataclass
os.system("clear||cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereco: str

    def exibindo_dados(self):
        print("\nExibindo dados")
        print(f"Nome: {self.nome}, idade: {self.email}, altura: {self.telefone}, Endereço: {self.endereco}")


nome = input("Digite seu nome: ")
email= input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")

pessoa1 = Pessoa(nome, email, telefone, endereco)
pessoa1.exibindo_dados()






