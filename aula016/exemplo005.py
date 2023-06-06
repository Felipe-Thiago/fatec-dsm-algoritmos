try:
    n1 = int(input("Informe um número inteiro: "))
except ValueError:
    print("Você não digitou um valor válido!")
else:
    print(f"Você digitou o número {n1}")
finally:
    print("Fim do bloco!")