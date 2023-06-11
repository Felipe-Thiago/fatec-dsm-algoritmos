"""while True:
    b = float(input("Digite o valor da base (maior que 0): "))
    if (b <= 0):
        print("Insira outro número!")
        continue
    break
while True:
    a = float(input("Digite o valor da altura (maior que 0): "))
    if (a <= 0):
        print("Insira outro número!")
        continue
    break
area = (a * b)/2
print(f"A área de um triângulo com esses valores é de {area:.2f}")"""

base = float(input("Digite a base do triângulo (maior que 0): "))
while base <= 0:
    base = float(input("Ops! Digite a base do triângulo MAIOR QUE 0: "))

while True:
    altura = float(input("Digite a altura do triângulo (maior que 0)"))
    if altura > 0:
        break

area = (base * altura)/2
print(f"A área do triângulo é de: {area:.2f}")