#Dada uma lista de números, encontre o maior número da lista sem usar a função max().

lista = [12, 45, 3, 67, 23, 89, 5]
numero = 0

for i in lista:
  if i > numero:
    numero = i

print(f"O maior número da lista é: {numero}")
  