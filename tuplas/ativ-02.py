# Crie uma tupla com alguns números inteiros. Peça ao usuário um número e diga se ele está ou não presente na tupla.

numeros = (3, 6, 1, 8, 4)

user = int(input("Adivinhe o número escondido: "))

if user in numeros:
  print("Você acertou.")
else:
  print("Você errou.")