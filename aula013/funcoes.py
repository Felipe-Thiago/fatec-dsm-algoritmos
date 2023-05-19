import random

def jogarDados():
    valor = random.randint(1,6)
    return valor

def desenha():

    for i in range(30):
        print("=", end="")

'''
print(f"{jogarDados()}")
'''
