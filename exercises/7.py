def dif_check(valores:list):
    return (valores[0]*valores[1])-(valores[2]*valores[3])

lista = [int(input()) for i in range(0,4)]


print(f"DIFERENCA = {dif_check(lista)}")
