import os
from dataclasses import dataclass
os.system("clear||cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: int
    endereco: str


nome = input("Digite seu nome: ")
email= input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
endereco = input("Digite seu endereço: ")

#Atrubuindo valores
pessoa1 = Pessoa(nome=nome, email=email, telefone=telefone, endereco=endereco)




print("===Dados cadastrados===")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.email}, altura: {pessoa1.telefone}, Endereço: {pessoa1.endereco}")


