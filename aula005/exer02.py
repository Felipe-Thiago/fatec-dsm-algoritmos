altura = float(input("Insira sua altura: "))
sexo = input("Homem ou Mulher?: ")
if (sexo == "homem") or (sexo == "Homem") or (sexo == "h" or "H"):
    peso = (72.7 * altura) - 58
    print(f"O peso ideal para você é de {peso} kg")
if (sexo == "mulher") or (sexo == "Mulher" or "M" or "m"):
    peso = (62.1 * altura) - 44.7
    print(f"O peso ideal para você é de {peso} kg")

    #alternativa: if sexo.upper() =="M": ------------ transforma minusculas (m) em maiusculas (M)