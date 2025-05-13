def calc_total(linhas, subtotal_lst = []):
    linhas =  [linha.split(" ") for linha in linhas]
    for linha in linhas:
        _, qtd, valor = linha
        subtotal_lst.append(int(qtd) * float(valor))
    return sum(subtotal_lst)

linhas = [input() for _ in range(0, 2)]


print(f"VALOR A PAGAR: R$ {calc_total(linhas):.2f}")
