int(minutos = 10)
int(segundos = 0)

for i in range(600, -1, -1):
    print(f"{minutos}:{segundos}")
    if seg == 0:
        seg == 60
    seg = seg - 1
