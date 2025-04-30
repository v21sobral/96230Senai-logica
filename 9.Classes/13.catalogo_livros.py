import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nAutor: {self.autor} \nCategoria: {self.categoria} \nPreço: {self.preco} \n\n")

lista_livros = []
QUANTIDADE_LIVROS = 3

for i in range(QUANTIDADE_LIVROS):
    livros = Livro(
                        nome = input("Digite o nome do livro: "), 
                        autor = (input("Digite o autor do livro: ")),
                        categoria = (input("Digite a categoria do livro: ")),
                        preco = float(input("Digite o preço do livro: "))
                        )
    

    lista_livros.append(livros)
    print("")


#Salnvando dados em arquivo txt
nome_arquivo = "Dados do livro.txt"
with open(nome_arquivo, "a") as catalogo_livros:
    for livros in lista_livros:
        catalogo_livros.write(f"{livros.nome}, {livros.autor}, {livros.categoria}, {livros.preco}\n")


print("Exibindo os dados da lista")
for livros  in lista_livros:
    livros.exibir_dados()