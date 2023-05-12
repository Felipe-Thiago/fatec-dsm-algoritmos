frase = input("Digite uma frase: ")

qtd = 0
for l in frase:
    if l.lower() in 'aeiouàáãâéèêíìîóòõôúùûäëïöü':
        qtd += 1
print(f"Na frase '{frase}' há {qtd} vogais")