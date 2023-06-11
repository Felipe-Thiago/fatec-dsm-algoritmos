print("Cálculo de subida de uma escada")
alt_deg = int(input("Insira a altura do degrau (em cm): "))
alt_tot = float(input("Insira a altura desejada (em metros): "))

degraus = round(alt_tot / (alt_deg/100))

print(f"Para subir {alt_tot} metros, você precisa subir {degraus} degraus")