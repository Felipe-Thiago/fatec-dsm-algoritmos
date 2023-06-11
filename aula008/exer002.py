data = input("Digite uma data (dd/mm/aaaa):")

#print("No formato AAAAMMDD, essa data é: " + data[6:10] + data[3:5] + data[0:2])

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]
nova_data = ano + mes + dia

print(f"No formado AAAAMMDD, essa data é {nova_data}")