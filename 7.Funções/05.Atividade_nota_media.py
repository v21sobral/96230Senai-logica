import os
os.system("cls || clear")

def mediaf(nota1, nota2):
    media_nota = (nota1 + nota2)/2
    return media_nota

def vmedia_nota(media):
    if media >= 7:
        return "aprovado"
    else:
        return "reprovado"

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
resultadomedia = mediaf(nota1, nota2)
vmedia_nota(resultadomedia)