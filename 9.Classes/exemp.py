import os
from dataclasses import dataclass
os.system("clear||cls")

@dataclass
class Persona:
    nome: str
    idade: int
    raca: str

#Atrubuindo valores
persona1 = Persona("Leandra", 30)
persona2 = Persona("Carla", 21)

pet1 = ("Pingo", 3, "Border Coller")
pet2 = ("Java", 7, "Doberman")

print("Dados das pessoas: ")
print(f"Nome: {persona1.nome}, idade: {persona1.idade}")
print(f"Nome: {persona2.nome}, idade: {persona2.idade}")

print("Dados dos pets: ")
print(f"Nome: {pet1.nome}, idade: {pet1.idade}, Raça: {pet1.raca}")
print(f"Nome: {pet2.nome}, idade: {pet2.idade}, Raça: {pet2.raca}")



