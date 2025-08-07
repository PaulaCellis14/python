#Dada uma tupla com 10 números aleatórios, crie uma nova tupla apenas com os números pares.
tupla = (30, 34, 62, 58, 51, 59, 7, 51, 50, 25)
lista_pares = []

for numero in tupla:
  if numero % 2 == 0:
    lista_pares.append(numero)

lista_pares = tuple(lista_pares)

print(lista_pares)