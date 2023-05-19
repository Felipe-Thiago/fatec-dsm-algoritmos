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

'''
    for i in range(1,11):
    print(fibonacci(i), end=" ")
'''

