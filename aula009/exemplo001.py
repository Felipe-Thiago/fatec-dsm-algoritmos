vetor = []
for i in range(5):
    x = int(input(f"Digite o {i+1}º valor: "))
    vetor.append(x)

print("Primeira forma: ", end=' ')
for i in range(4, -1, -1):
    print(vetor[i], end=' ')

print(end='\n')
print("Segunda forma:", vetor[::-1])


vetor.reverse()
print("Terceira forma:", vetor)
vetor.reverse()
print(vetor)