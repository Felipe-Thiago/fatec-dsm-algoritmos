#Faça um programa que calcule os 10 primeiros números da sequencia de Fibonacci
n = int(input("Entre com um número inteiro positivo: "))
a = 0
b = 1
print(a)
for i in range(1,n):
    print(b)
    a, b = b, a+b