def salario_bonus(salario, vendas):
    bonus = vendas * 0.15
    return salario + bonus
    

nome = input()
salario = float(input())
vendas = float(input())

print(f"TOTAL = R$ {salario_bonus(salario, vendas):.2f}")