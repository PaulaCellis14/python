#Crie uma tupla que represente uma matriz 3x3:
#Imprima a diagonal principal.
#Calcule a soma de todos os elementos.

matriz = (
  (1, 2, 3),
  (4, 5, 6),
  (7, 8, 9)
)

print(matriz[0][0], matriz[1][1], matriz[2][2])

soma = 0

for tupla in matriz:
  for elemento in tupla:
    soma += elemento

print(soma)