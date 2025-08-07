# Crie uma tupla com números inteiros.
# Conte quantas vezes o número 5 aparece nela sem usar o método .count() — apenas com um laço for.

numeros = (8, 4, 10, 5, 13, 98, 5, 37, 5, 15, 63, 7, 5)
quantidade_5 = 0

for numero in numeros:
  if numero == 5:
    quantidade_5 += 1
  else:
    continue

print(f"O número 5 aparece {quantidade_5} vezes na sequência")