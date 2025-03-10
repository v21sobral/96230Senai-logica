import os
os.system("clear")



nome_aluno = input("Digite seu nome: ")
nota1_aluno = float(input("Digite a nota da primeira prova: "))
nota2_aluno = float(input("Digite a nota da primeira prova: "))
media_aluno = (nota1_aluno + nota2_aluno)/2


if media_aluno >= 9:
    print(f"(A) Parabéns! Você foi aprovado com média: {media_aluno:.1f}")
elif media_aluno < 9 and media_aluno >= 7.5:
    print(f"(B) Parabéns! Você foi aprovado com média: {media_aluno:.1f}")
elif media_aluno < 7.5 and media_aluno >= 6:
    print(f"(C) Parabéns! Você foi aprovado com média: {media_aluno:.1f}")
elif media_aluno < 6 and media_aluno >= 4:
    print(f"(D) Você foi reprovado com média: {media_aluno:.1f}")
    print("Você poderá fazer uma prova final substitutiva.")
elif media_aluno < 6 and media_aluno >= 4:
    print(f"(E) Você foi reprovado com média: {media_aluno:.1f}")
    print("Você terá que repipitir a matéria no próximo ano.")
