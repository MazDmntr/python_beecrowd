def calc_media(a:float, b:float):
    nota1 = a * 3.5
    nota2 = b * 7.5
    return ((nota1 + nota2) / 11)

a = float(input())
b = float(input())

print(f"MEDIA = {calc_media(a,b):.5f}")
