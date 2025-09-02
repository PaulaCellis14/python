#Crie um programa que recebe dois conjuntos e exibe a interseção deles.

moveis_paula = set()
moveis_karol = set()

for i in range(5):
  quarto_paula = input(f"Digite o {i+1}º móvel do quarto de Paula: ").capitalize()
  moveis_paula.add(quarto_paula)

for i in range(5):
  quarto_karol = input(f"Digite o {i+1}º móvel do quarto de Karol: ").capitalize()
  moveis_karol.add(quarto_karol)

print("No quarto de Paula há:")
print(moveis_paula)
print()

print("No quarto de Karol há:")
print(moveis_karol)
print()

print("No quarto de ambas há:")
print(moveis_paula & moveis_karol)