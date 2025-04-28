import os
from dataclasses import dataclass
os.system("clear||cls")

@dataclass
class Pessoa:
    nome: str
    idade: int
    altura: float
    peso: float

#Atrubuindo valores
pessoa1 = Pessoa("Leandra", 30, 66, 50.5)
pessoa2 = Pessoa("Carla", 21, 56, 61.8)



print("Dados das pessoas: ")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}, altura: {pessoa1.altura}, peso: {pessoa1.peso}")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade}, altura: {pessoa2.altura}, peso: {pessoa2.peso}")

