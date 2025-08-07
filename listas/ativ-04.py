#Dada uma lista de nomes, exiba cada nome junto com o seu índice usando enumerate().
nomes = ["Ana", "Carlos", "Beatriz", "Diego", "Fernanda", "Lucas"]

for indice, nome in enumerate(nomes):
  print(f"Índice: {indice}: {nome}")