def pegaSobrenome():
    while True:
        sobrenome = input("Digite o sobrenome: ")
        if sobrenome:
            if sobrenome.isalpha():
                return sobrenome
            else:
                print("Digite um sobrenome válido")
        else:
            return sobrenome

def pegaIdade():
    while True:
        try:
            idade = int(input("Digite uma idade: "))
        except:
            print("Digite uma idade válida")
        else:
            if idade:
                return idade
            else:
                print("Digite uma idade válida")

def pegaAltura():
    while True:
        try:
            altura = int(input("Digite uma altura (em cm): "))
        except:
            print("Digite uma altura válida, em centímetros! (inteiro)")
        else:
            if altura:
                return altura
            else:
                print("Digite uma altura válida (inteiro)")

def pegaPeso():
    while True:
        try:
            peso = float(input("Digite um peso (em kg): "))
        except:
            print("Digite um peso válido!")
        else:
            if peso:
                return peso
            else:
                print("Digite um peso válido!")

pessoas = []
n=0

while True:
    sobrenome = pegaSobrenome()
    if sobrenome:
        n+= 1
        idade = pegaIdade()
        altura = pegaAltura()
        peso = pegaPeso()

        pessoa = [sobrenome, idade, altura, peso]
        pessoas.append(pessoa)
    else:
        break

soma_idade = 0
soma_altura = 0
soma_peso = 0


if n>0:
    pessoas.sort()
    print("Relação de nomes cadastrados...")
    print("----------------------------------------")

    for i in range(0, len(pessoas)):
        print(f"{pessoas[i][0]:10} - {pessoas[i][1]} - {pessoas[i][2]} - {pessoas[i][3]:5.1f}")
        soma_idade += pessoas[i][1]
        soma_altura += pessoas[i][2]
        soma_peso += pessoas[i][3]
    print("----------------------------------------")
    media_idade = soma_idade/n
    media_altura = soma_altura/n
    media_peso = soma_peso/n
    print(f"Idade média: {media_idade}")
    print(f"Altura média: {media_altura}")
    print(f"Peso médio: {media_peso}")
    print("----------------------------------------")
