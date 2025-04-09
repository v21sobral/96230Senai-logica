import os
os.system("cls || clear")
from datetime import date

def ano_idade(data):
   idade = date.today().year - data
   return idade


data = int(input("Digite o ano que nasceu: "))

idade = ano_idade(data)

print(f"A sua idade é: {idade} anos")
