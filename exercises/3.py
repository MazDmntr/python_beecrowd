raio = float(input())

def calcula_area(raio, pi=3.14159):
    return pi * pow(raio, 2)

area = calcula_area(raio)

print(f"A={round(area,4):.4f}")
