frase = input("Digite uma frase: ")

qtd = 0
qtda = 0
qtde = 0
qtdi = 0
qtdo = 0
qtdu = 0

for l in frase:
    if l.lower() == 'a':
        qtd += 1
        qtda += 1
    if l.lower() == 'e':
        qtd += 1
        qtde += 1
    if l.lower() == 'i':
        qtd += 1
        qtdi += 1
    if l.lower() == 'o':
        qtd += 1
        qtdo += 1
    if l.lower() == 'u':
        qtd += 1
        qtdu += 1
print(f"Na frase '{frase}' há {qtd} vogais, sendo {qtda} da letra 'a', {qtde} da letra 'e', {qtdi} da letra 'i', {qtdo} da letra 'o' e {qtdu} da letra 'u'")