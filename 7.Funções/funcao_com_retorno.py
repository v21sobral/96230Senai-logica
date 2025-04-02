import os

os.system("cls || clear")

def calculo_media(primeira_nota, segunda_nota):
    soma = primeiro_numero + segundo_numero
    media_nota = soma / 2
    return media_nota

primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o sgundo numero: "))

media = calculo_media(primeiro_numero, segundo_numero)

print(f"Média: {media:.1f}")