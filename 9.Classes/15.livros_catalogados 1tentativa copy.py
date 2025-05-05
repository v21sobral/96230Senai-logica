import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Autor:
    nome: str
    bibliografia: str



@dataclass
class Livro:
    titulo: str
    autor: Autor
    ano: int

    def exibir_dados(self):
        print(f"Nome: {self.titulo} \nAno: {self.ano} \nAutor: {self.autor.nome} \n\n")

lista_livros = []


livros = Livro(
                        titulo = input("Digite o nome do livro: "), 
                        ano = int(input("Digite a ano do livro: ")),
                        autor = Autor(
                         nome = input("Digite o autor do livro: "),
                         bibliografia = input("Digite o bibliografia do livro: ")
                        )
)

lista_livros.append(livros)
print("")


#Salnvando dados em arquivo txt
nome_arquivo = "Dados do livro.txt"
with open(nome_arquivo, "a") as catalogo_livros:
    for livros in lista_livros:
        catalogo_livros.write(f"{livros.titulo}, {livros.ano}, {livros.autor}\n")


print("Exibindo os dados da lista")
for livros  in lista_livros:
    livros.exibir_dados()