num = int(input("Insira um número primo: "))

def primoounao(num):
    cont = 0

    for i in range(1, num+1):
        if (num%i)==0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False

def qtdprimos(num):
    j = 1
    primo = 0

    while primo < num:
        if primoounao(j):
            primo += 1
            print(primo)
        j += 1
    return primo


    #2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31

print(primoounao(num))
