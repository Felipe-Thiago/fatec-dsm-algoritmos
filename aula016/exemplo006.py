def divisao(a, b):
    """try:
        return int(a)/int(b)
    except(ValueError, ZeroDivisionError) as erro:
        return f"Ocorreu algum problema: {erro}"
    """
try:
    n1 = int(input("Informe o dividendo: "))
except:
    print("Precisa ser um número inteiro!")
else:
    try:
        n2 = int(input("Informe o divisor: "))
    except:
        print("Precisa ser um número inteiro!")
    else:
        try:
            print(divisao(n1/n2))
        except:
            print("Erro na divisão!")
finally:
    print("Fim da execução")