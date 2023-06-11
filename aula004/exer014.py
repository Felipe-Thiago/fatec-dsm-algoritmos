print("Cálculo de horas em minutos")
valor = float(input("Insira uma quantidade de tempo com horas e minutos (ex.: 3.20 para 3 horas e 20 minutos): "))

hora = int(valor)
minutos = (valor - hora) * 100
minutos_tot = (hora * 60) + minutos

print(f"{valor} horas possui {minutos_tot:.2f} minutos")