nome = input("Digite seu primeiro nome: ")
nome_meio = input("Digite seu nome do meio: ")
sobrenome = input("Digite seu sobrenome: ")

completo = nome + ' ' + nome_meio + ' ' + sobrenome

print(f"Nome completo: {completo}")



nome_cripto = ''
for i in range(0, len(completo)):
    #print(completo[i], end=" ")
    nome_cripto += (chr(ord(completo[i]) + 1))

print(f"Nome criptografado: {nome_cripto}")