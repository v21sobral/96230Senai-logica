import os
os.system("cls || clear")

def logo_senai():
    os.system("cls||clear")
    print("|==Você é o futuro você é SENAI==|")

def mostra_soma(primeira_numero, segunda_nnumero):
 return primeiro_numero + segundo_numero

def mostra_subtracao(primeiro_numero, segundo_numero):
 if primeiro_numero > segundo_numero:
  return primeiro_numero - segundo_numero
 elif primeiro_numero < segundo_numero:
   return segundo_numero - primeiro_numero
 else:
   return 0

def mostra_multiplicacao(primeira_numero, segunda_nnumero):
 return primeiro_numero * segundo_numero

def mostra_divisao(primeira_numero, segunda_nnumero):
 if primeiro_numero == 0:
  return print("Não é possível dividir por 0")
 else:
  return primeiro_numero / segundo_numero


logo_senai()
primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o sgundo numero: "))

soma = mostra_soma(primeiro_numero, segundo_numero)
subtracao = mostra_subtracao(primeiro_numero, segundo_numero)
multiplicacao = mostra_multiplicacao(primeiro_numero, segundo_numero)
divisao = mostra_divisao(primeiro_numero, segundo_numero)

print(f"Soma: {soma:.1f}")
print(f"Subtração: {subtracao:.1f}")
print(f"Multiplicação: {multiplicacao:.1f}")
print(f"Divisão: {divisao:.1f}")