def calc_salario(dias, valor):
    return dias * valor

a = int(input())
b = int(input())
c = float(input())

print(f"NUMBER = {a}")
print(f"SALARY = U$ {calc_salario(b, c):.2f}")
