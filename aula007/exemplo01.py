soma = 0
n = 0

for x in range(1,11):
    idade = int(input(f'Digite a {x}ª idade: '))
    if x == 5:
        continue
    soma += idade
    n = n + 1

print(x, 'repetições')
print(n, 'somas')
media = soma/n
print(f'A média das idades é de {media:.2f}')