def calcula_media(valores:list):
    pesos = [2, 3, 5]
    notas = [valor * peso for valor, peso in zip(valores, pesos)]
    resultado = sum(notas)/10
    
    return resultado

valores = [float(input()) for valor in range(0,3)]

print(f"MEDIA = {calcula_media(valores):.1f}")
