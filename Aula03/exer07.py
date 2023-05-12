print("Conversão de valores bizarros dos EUA: \n")
pes = float(input("Entre com um valor em pés (?): "))

polegadas = pes*12
jarda = pes/3
milha = jarda/1760


#print(f"O valor de {pes:.2f} pés equivale a {polegadas:.2f} polegadas, {jarda:.2f} jardas e {milha:.2f} milhas")
print(f"Polegadas: {polegadas:.2f}")
print(f"Jardas: {jarda:.2f}")
print(f"Milha: {milha:.2f}")