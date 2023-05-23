ra = 3011392313027
todo = []
def pacos(totCab, totPes):
    C = (totPes-(2*totCab))/2
    P = totCab - C

    todo.append(C)
    todo.append(P)
    return todo

totCab = int(input("Total de Cabeças: "))
totPes = int(input("Total de Pés: "))
pacos(totCab, totPes)

print(f"Total de Patos: {todo[1]}")
print(f"Total de Coelhos: {todo[0]}")