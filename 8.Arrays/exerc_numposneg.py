import os
os.system("clear")

numeros = []
print("NÚMEROS POSITIVOS E NEGATIVOS")
lista_numero = []

def positivos_negativos(lista):
    positivo = 0
    negativo = 0
    neutro = 0
    for numero in lista:
        if numero == 0:
            neutro += 1
        elif numero < 0:
            negativo += 1
        elif numero > 0:
            positivo += numero  # Soma os números positivos
    return negativo, positivo, neutro

# Define a quantidade de números a serem inseridos
QUANTIDADE_NUMEROS = 5
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f'Digite o {i+1}ª número: '))
    lista_numero.append(numero)

# Chama a função e atribui os resultados
negativo, resutposit, neutro = positivos_negativos(lista_numero)

# Exibe os resultados
print("")
print(f"Soma dos números positivos: {resutposit}")
print(f"Números negativos: {negativo}")
print(f"Números neutros: {neutro}")

