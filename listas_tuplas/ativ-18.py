#Crie uma lista com valores repetidos e remova todos os duplicados, mantendo a ordem original.

valores = [3, 5, 2, 3, 7, 5, 9, 2, 1, 7, 4]
sem_duplicatas = []

for i in valores:
  if i not in sem_duplicatas:
    sem_duplicatas.append(i)

print(sem_duplicatas)