import os
os.system("cls||clear")
import time

logar = []

def cadastro():
    while True:
        print("=== Faça seu cadastro para acessar o sistema ===\n")
        cadastrar = input("Informe seu número de matrícula para cadastro: ")
        cadastrarS = input("Informe sua senha para cadastro: ")
        logar.append({"login":cadastrar, "senha":cadastrarS})

        continuar_login = input("Deseja cadastrar outro usuário? (S/N): ").lower()
        if continuar_login != 's':
            break
    os.system("cls||clear")

def login():
    bloqueio = 3
    while bloqueio > 0:
        print("=== Informe seu login para acessar o sistema ===\n")
        login_final = input("Informe sua matrícula: ")
        loginS_final = input("Informe sua senha: ")
     
        for funcionario in logar:
            if funcionario["login"] == login_final and funcionario["senha"] == loginS_final:
                print("Login bem-sucedido!")
                time.sleep(2)
                os.system("cls||clear") 
                return True
        print("Login ou senha incorretos. Tente novamente...")
        bloqueio -= 1
        time.sleep(1)
        os.system("cls||clear") 
    print("Você excedeu o limite de tentativas.")
    return False

def inss(salario):
    if salario <= 1320.00:
        return salario * 0.075
    elif salario <= 2571.29:
        return (1320.00 * 0.075) + ((salario - 1320.01) * 0.09)
    elif salario <= 3856.94:
        return (1320.00 * 0.075) + ((2571.29 - 1320.01) * 0.09) + ((salario - 2571.30) * 0.12)
    elif salario <= 7507.49:
        desconto = (1320.00 * 0.075) + ((2571.29 - 1320.01) * 0.09) + ((3856.94 - 2571.30) * 0.12) + ((salario - 3856.95) * 0.14)
        return min(desconto, 1051.05)
    else:
        return 1051.05
         
def irrf(salario_bruto, necessitados):
    deducaoPnecessitado = 189.59 * necessitados
    calculo_salario = salario_bruto - inss(salario_bruto) - deducaoPnecessitado
    if calculo_salario <= 2112.00:
        return 0
    elif calculo_salario <= 2826.65:
        return calculo_salario * 0.075 - 158.40
    elif calculo_salario <= 3544.00:
        return calculo_salario * 0.15 - 370.40
    elif calculo_salario <= 4256.00:
        return calculo_salario * 0.225 - 651.73
    else:
        return calculo_salario * 0.275 - 884.96

# Sistema principal
cadastro()
if login():
    salario_bruto = float(input("Informe seu salário bruto (R$): "))
    necessitados = int(input("Informe o número de dependentes: "))
    vale_transporte = input("Deseja receber vale transporte? (S/N): ").lower()
    vale_refeicao = float(input("Digite o valor do vale refeição oferecido pela empresa (R$): "))
    
    # Cálculos
    desconto_inss = inss(salario_bruto)
    desconto_irrf = irrf(salario_bruto, necessitados)
    desconto_valeRF = vale_refeicao * 0.20
    desconto_planoS = 150.00 * necessitados

    if vale_transporte == 's':
        desconto_valeT = salario_bruto * 0.06
    else:
        desconto_valeT = 0

    descontos_total = (desconto_inss + desconto_planoS + desconto_valeT + desconto_valeRF + desconto_irrf)
    salario_liquido = salario_bruto - descontos_total

    # Exibição formatada conforme os exemplos
    print("\n============ Folha de Pagamento ============")
    print(f"Salário Base: R$ {salario_bruto:.2f}")
    print(f"Dependentes: {necessitados}")
    print(f"Vale Transporte: {'Sim' if vale_transporte == 's' else 'Não'}")
    print(f"Vale Refeição: R$ {vale_refeicao:.2f}")
    print("--------------------------------------------")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")
    print("============================================")