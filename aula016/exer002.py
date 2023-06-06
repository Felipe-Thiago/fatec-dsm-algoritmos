def pegaModelo():
    while True:
        try:
            modelo = input("Insira um modelo de carro: ")
        except:
            print("Ocorreu algum erro!")
        else:
            if modelo:
                return modelo
            else:
                print("Ocorreu algum erro!")

def pegaConsumo():
    while True:
        try:
            consumo = float(input("Insira o consumo do carro (km/h): "))
        except:
            print("Ocorreu algum erro!")
        else:
            if consumo:
                return consumo
            else:
                print("Ocorreu algum erro!")


carros = []
n = 0
num = 0

for i in range(1, 6):
    n += 1

    modelo = pegaModelo()
    if modelo:
        consumo = pegaConsumo()
        num += 1

        carro = [num, modelo, consumo]
        carros.append(carro)
    else:
        break

mais_eco = 0
gasto_mil = 0
custo_mil = 0

if n > 0:
    carros.sort()
    print("Relação de carros registrados")
    print("----------------------------------------")

    for i in range(0, len(carros)):
        print(f"{carros[i][0]} - {carros[i][1]} - {carros[i][2]} km/h")