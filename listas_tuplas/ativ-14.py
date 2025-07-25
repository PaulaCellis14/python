#Crie uma lista com 10 números. Imprima apenas os números pares usando um loop.

numeros = [3, 6, 8, 1, 5, 9, 2, 4, 7, 0]

for num in numeros:
  if num == 0:
    continue
  if num % 2 == 0:
    print(f"{num} é um número par.")