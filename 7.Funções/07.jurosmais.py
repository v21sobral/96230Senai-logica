import os
os.system("cls || clear")

def inflacionar(preco):
    if preco < 100:
        resultado = preco * 1.10
    else:
        resultado = preco * 1.20
    return resultado

def desconto(preco):
    if preco < 100:
        resultado = preco * 0.10
    else:
        resultado = preco * 0.20
    return resultado

preco_produto = float(input("Digite o preço do produto: "))
preco_inflacionado = inflacionar(preco_produto)
preco_descontado = desconto(preco_produto)
precodesconto_total = preco_produto - preco_descontado

print(f"O preço do produto com desconto é: R$ {precodesconto_total:.2f}")
print(f"O preço do produto com inflação é: R$ {preco_inflacionado:.2f}")