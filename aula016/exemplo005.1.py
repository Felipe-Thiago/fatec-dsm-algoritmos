def entrada():
    try:
        n1 = int(input("Informe um número inteiro: "))
    except:
        return None
    else:
        return n1
    finally:
        print("Fim do bloco!")

a = entrada()
print(a)