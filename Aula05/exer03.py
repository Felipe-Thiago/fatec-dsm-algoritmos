print("====================================")
print("Cálculo de tinta necessária")
print("====================================\n")
largura = float(input("Insira a largura, em metros, do aposento: "))
comprimento = float(input("Insira o comprimento, em metros, do aposento: "))
tintadisp = float(input("Insira a quantidade de tinta, em litros, disponível: "))

print("\n====================================\n\n")

apintar = (comprimento * 2.80 * 2) + (largura * 2.80 * 2) - 1.68
tintanesc = apintar/3


print(f"Você precisará pintar {apintar:.2f} m² de parede.")
if(tintanesc%3 != 0):
    print(f"A quantidade de latas de tinta necessária para isso é de {tintanesc - tintanesc%3 + 1}")
else:
    print(f"A quantidade de latas de tinta necessária para isso é de {tintanesc}")


tintafalta = tintanesc - tintadisp
print(f"Com a quantidade que você tem, ainda faltam mais {tintafalta:.2f} litros, ou {(tintafalta - tintafalta%3 + 1)} latas.")