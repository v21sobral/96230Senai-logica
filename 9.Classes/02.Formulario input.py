import os
from dataclasses import dataclass
os.system("clear||cls")

@dataclass
class Pessoa:
    nome: str
    idade: int
    altura: float
    peso: float

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")
peso = input("Digite seu peso: ")

#Atrubuindo valores
pessoa1 = Pessoa(nome=nome, idade=idade, altura=altura, peso=peso)




print("Dados das pessoas: ")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}, altura: {pessoa1.altura}, peso: {pessoa1.peso}")


