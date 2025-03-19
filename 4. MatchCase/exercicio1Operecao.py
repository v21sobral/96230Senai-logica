import os
os.system("clear")

print("Calculadora")

numero_um = float(input("Digite um número: "))
operacao = input("Você deseja (+ - * /)?:")
numero_dois = float(input("Digite um número: "))


match operacao:
    case "+":
        resultado = numero_um + numero_dois
    case "-":
        resultado = numero_um - numero_dois
    case "*":
        resultado = numero_um * numero_dois
    case "/":
        resultado = numero_um / numero_dois
    case _:
        resultado = "operação inválida"
    


print(f"\nResultado foi: {numero_um} {operacao} {numero_dois} = {resultado}")