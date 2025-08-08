#Crie um programa que recebe dois conjuntos e exibe a interseção deles.

ano_2024 = "sim"
ano_2025 = "sim"

mediuns_2024 = set()
mediuns_2025 = set()

while ano_2024 == "sim":
  med_2024 = str(input("Quais os médiuns que estavam na casa em 2024? ")).strip().capitalize()
  mediuns_2024.add(med_2024)

  ano_2024 = str(input("Teria mais algum nome para acrescentar? ")).strip().lower()

  print(mediuns_2024)

while ano_2025 == "sim":
  med_2025 = str(input("Quais os mediuns que estavam na casa em 2025? ")).strip().capitalize()
  mediuns_2025.add(med_2025)

  ano_2025 = str(input("Teria mais algum nome para acrescentar? ")).strip().lower()

  print(mediuns_2025)

print('Os médiuns presentes nos dois anos são:')
print(mediuns_2024.intersection(mediuns_2025))