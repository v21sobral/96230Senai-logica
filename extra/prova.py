def calcular_inss(salario):
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

def calcular_irrf(salario_base, dependentes):
    deducao_dependente = 189.59 * dependentes
    base_calculo = salario_base - calcular_inss(salario_base) - deducao_dependente
    
    if base_calculo <= 2112.00:
        return 0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 158.40
    elif base_calculo <= 3544.00:
        return base_calculo * 0.15 - 370.40
    elif base_calculo <= 4256.00:
        return base_calculo * 0.225 - 651.73
    else:
        return base_calculo * 0.275 - 884.96

def main():
    print("Sistema de Folha de Pagamento")
    print("-----------------------------")
    
    # Autenticação (simplificada para o exercício)
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    
    # Dados do funcionário
    salario_base = float(input("Digite seu salário base (R$): "))
    dependentes = 1  # Considerando 1 dependente conforme observação
    opcao_vale_transporte = input("Deseja receber vale transporte? (s/n): ").lower()
    vale_refeicao = float(input("Digite o valor do vale refeição fornecido (R$): "))
    
    # Cálculos
    desconto_inss = calcular_inss(salario_base)
    
    if opcao_vale_transporte == 's':
        desconto_vale_transporte = salario_base * 0.06
    else:
        desconto_vale_transporte = 0
    
    desconto_vale_refeicao = vale_refeicao * 0.20
    desconto_plano_saude = 150.00 * dependentes
    desconto_irrf = calcular_irrf(salario_base, dependentes)
    
    # Total de descontos
    total_descontos = (desconto_inss + desconto_vale_transporte + 
                       desconto_vale_refeicao + desconto_plano_saude + 
                       desconto_irrf)
    
    # Salário líquido
    salario_liquido = salario_base - total_descontos
    
    # Exibição dos resultados
    print("\n--- Demonstrativo de Pagamento ---")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"Desconto INSS: R$ {desconto_inss:.2f}")
    print(f"Desconto IRRF: R$ {desconto_irrf:.2f}")
    print(f"Desconto Vale Transporte: R$ {desconto_vale_transporte:.2f}")
    print(f"Desconto Vale Refeição: R$ {desconto_vale_refeicao:.2f}")
    print(f"Desconto Plano de Saúde: R$ {desconto_plano_saude:.2f}")
    print("----------------------------------")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

if __name__ == "__main__":
    main()