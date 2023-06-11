from math import pow, pi

""" ou
import math
math.pow(2, 2)
math.pi
"""

print("Cálculo da área de um círculo. \n")
raio = float(input("Entre com o valor do raio: "))


area = pi * pow(raio, 2)

print(f"A área do círculo é de {area:7.3f} cm²")