vetor = [0]*5
vetor2 = [0]*5
vetor3 = []

for i in range(5):
    vetor[i] = int(input(f"Insira o {i+1}º valor do primeiro vetor: "))

for i in range(5):
    vetor2[i] = int(input(f"Insira o {i+1}º valor do primeiro vetor: "))

for i in range(5):
    vetor3.append(vetor[i])
    vetor3.append(vetor2[i])

print(vetor3)