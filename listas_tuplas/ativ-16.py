#Dada a lista lista = [1, 2, 3, 4, 5, 6], inverta os elementos de dois em dois usando for e range().

lista = [1, 2, 3, 4, 5, 6]

for i in range(0, len(lista)-1, 2):
  lista[i], lista[i+1] = lista[i+1], lista[i]

print(lista)