

num = [0]*10
ind = 0
a = 0
x = 101
while a < 10:
    primo = False
    div = 0
    for i in range(1, x):
        if (x % i) == 0:
            div = div + 1

    if div == 1:
        primo = True
        

    if primo:
        num[ind] = x
        ind = ind + 1
        a +=1
    x += 1

print(num)