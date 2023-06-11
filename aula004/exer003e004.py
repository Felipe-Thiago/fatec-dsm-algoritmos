anonasc = int(input("Bem-vindo, entre com seu ano de nascimento: "))
anoatual = int(input("Em que ano estamos?: "))

idade_anos = (anoatual - anonasc)
idade_meses = (idade_anos * 12)
#idade_dias = (idade_meses * 30)
idade_dias2 = (idade_anos * 365)
#idade_semanas = (idade_meses * 4)
idade_semanas2 = (idade_anos * 35)

#print("Sua idade em anos:", idade_anos)
#print("Sua idade em meses é de aproximadamente", idade_meses)
#print("Sua idade em dias é de aproximadamente", idade_dias2)
#print("Sua idade em semanas é de aproximadamente", idade_semanas2)


print(f"Você tem {idade_anos} anos ou {idade_meses} meses")
print(f"ou {idade_semanas2} semanas ou {idade_dias2} dias")