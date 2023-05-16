h = input("Digite um horário (formato 00:00:00): ")

hn = h.split(":")

h = int(hn[0])
m = int(hn[1])
s = int(hn[2])

def converter(h, m, s):
    hs = h * 3600
    ms = m * 60

    seg = hs + ms + s
    return seg

if h > 23:
    print("Horário inválido")
else:
    if m > 60:
        print("Horário inválido")
    else:
        if s > 60:
            print("Horário inválido")

print(f"O total deste horário é igual a {converter(h,m,s)} segundos")