def fibonacci(i):
    ''' Retorna o i-ésimo número da sequência de Fibonacci
            fibonacci(n)
        '''
    if i == 0:
        return 0
    if i == 1:
        return 1
    else:
        return fibonacci(i-1)+fibonacci(i-2)

x = int(input("Insira um limite para a sequência de Fibonacci: "))

for i in range(1, x+1):
    print(fibonacci(i), end=" ")