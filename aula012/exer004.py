def ehbis(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            return False
        else:
            return True
    else:
        if ano%400 == 0:
            return True
        else:
            return False

ano = int(input("Insira um ano: "))
if ehbis(ano):
    print(f"O ano {ano} é bissexto")
else:
    print(f"O ano {ano} não é bissexto")