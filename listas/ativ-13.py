# Crie uma lista com números repetidos e remova todos os elementos duplicados sem usar set(). Mantenha a ordem original.

numeros = [5, 3, 8, 3, 1, 9, 5, 2, 7, 4, 8, 6, 1, 10, 2, 9, 7, 6, 4, 10]
numeros_unicos = []

for num in numeros:
  if num not in numeros_unicos:
    numeros_unicos.append(num)
print("A sequência sem números duplicados é:", numeros_unicos)