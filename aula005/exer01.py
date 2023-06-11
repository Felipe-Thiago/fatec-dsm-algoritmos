p1 = float(input("Insira a nota 1: "))
p2 = float(input("Insira a nota 2: "))
p3 = float(input("Insira a nota 3: "))
media = (p1 + p2 + p3)/3

#if (media < 3):
#    print("Reprovado!")
#elif (media >= 3) and (media < 7):
    #print("Exame...")
    
#else:
#    print("Aprovado!")

if media >= 7:
    print(f"Sua média é {media:.1f}. Aprovado!")
else:
    if media >=3:
        print(f"Sua média é {media:.1f}. Exame!")
        nota = 12 - media
        print(f"Você precisa tirar no mínimo nota {nota:.1f} para passar.")
    else:
        print(f"Sua média é {media:.1f}. Reprovado!")