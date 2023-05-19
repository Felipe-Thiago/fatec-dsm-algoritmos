def numTriang(n):
    for i in range(3, n+1):
        if (i-2)*(i-1)*(i) == n:
            return True
    return False

n = int(input("Insira um número para ver se é triangular: "))
numTriang(n)



''' acima é o exemplo do professor, minha tentativa (incompleta):
for i in range(inic,num):
    if (inic * (inic-2) * (inic-1)) == num:
        print(f"O número {num} é triangular!")
    else:
        print(f"O número {num} não é triangular...")
    inic += 1
'''