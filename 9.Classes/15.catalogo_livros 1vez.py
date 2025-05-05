import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Livro:
    nome: str
    autor: str
    ano: int
    bibliografia: str

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nAutor: {self.autor} \nano: {self.ano} \nPreço: {self.bibliografia} \n\n")

lista_livros = []


livros = Livro(
                        nome = input("Digite o nome do livro: "), 
                        autor = input("Digite o autor do livro: "),
                        ano = int(input("Digite a ano do livro: ")),
                        bibliografia = input("Digite o bibliografia do livro: ")
                        )
    

lista_livros.append(livros)
print("")


#Salnvando dados em arquivo txt
nome_arquivo = "Dados do livro.txt"
with open(nome_arquivo, "a") as catalogo_livros:
    for livros in lista_livros:
        catalogo_livros.write(f"{livros.nome}, {livros.autor}, {livros.ano}, {livros.bibliografia}\n")


print("Exibindo os dados da lista")
for livros  in lista_livros:
    livros.exibir_dados()