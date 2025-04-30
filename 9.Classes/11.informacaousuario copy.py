import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoas:
    nome: str
    idade: int
    peso: float
    altura: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade} \nPeso: {self.peso} \nAltura: {self.altura} \n\n")

lista_cadastro = []
QUANTIDADE_PESSOAS = 4

for i in range(QUANTIDADE_PESSOAS):
    pessoas = Pessoas(
                        nome = input("Digite seu nome: "), 
                        idade = int(input("Digite sua idade: ")),
                        peso = float(input("Digite seu peso: ")),
                        altura = float(input("Digite sua altura: "))
                        )
    

    lista_cadastro.append(pessoas)
    print("")


print("Exibindo os dados da lista")
for pessaos  in lista_cadastro:
    pessoas.exibir_dados()