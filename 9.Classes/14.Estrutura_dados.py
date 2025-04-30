import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoas:
    nome: str
    data_nascimento: str
    rg: str
    cpf: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nData de nascimento: {self.data_nascimento} \nRG: {self.rg} \nCPF: {self.cpf} \n\n")

lista_usuario = []
QUANTIDADE_USUARIOS = 5

for i in range(QUANTIDADE_USUARIOS):
    usuarios = Pessoas(
                        nome = input("Digite o nome do livro: "), 
                        data_nascimento = int(input("Digite o data_nascimento do livro: ")),
                        rg = int(input("Digite a rg do livro: ")),
                        cpf = float(input("Digite o preço do livro: "))
                        )
    

    lista_usuario.append(usuarios)
    print("")


#Salnvando dados em arquivo txt
nome_arquivo = "Dados do livro.txt"
with open(nome_arquivo, "a") as catalogo_usuarios:
    for usuarios in lista_usuario:
        catalogo_usuarios.write(f"{usuarios.nome}, {usuarios.data_nascimento}, {usuarios.rg}, {usuarios.cpf}\n")


print("Exibindo os dados da lista")
for usuarios  in lista_usuario:
    usuarios.exibir_dados()