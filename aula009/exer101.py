vetor = [0]*10

for i in range(10):
    vetor[i] = int(input(f"Insira o {i + 1}º número inteiro: "))

vetor.reverse()
print(vetor)