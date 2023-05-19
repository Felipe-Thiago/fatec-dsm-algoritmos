import funcoes

funcoes.desenha()
print()

print("Bem-vindo ao jogo de dados.")

funcoes.desenha()
print()

while True:
    jogadaUser = input("Deseja realizar uma jogada? (Y/N)")
    if jogadaUser == "N":
        print()
        print("Tudo bem, volte novamente outra hora")
        break
    elif jogadaUser == "Y":
        valor = funcoes.jogarDados()
        valorpc = funcoes.jogarDados()
        print(f"Você lançou o dado e ele caiu no número {valor}!")

        funcoes.desenha()
        print()
        for _ in range(1, 100000000):
            pass
        print(f"O computador também fez uma jogada e caiu no número {valorpc}!")

        funcoes.desenha()
        print()

        for _ in range(1, 100000000):
            pass

        if valorpc > valor:
            print("Computador ganhou!")
        else:
            if valorpc == valor:
                print("Deu empate!")
            else:
                print("Você ganhou!!!")

        funcoes.desenha()
        print()

    else:
        print()
        print("Digite uma opção válida")
        funcoes.desenha()
        print()
