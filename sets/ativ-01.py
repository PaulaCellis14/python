#Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.

paula = set()
karol = set()

for i in range(3):
  cor_paula = input(f"Digite a {i+1}ª cor favorita de Paula: ").capitalize()
  paula.add(cor_paula)

for i in range(3):
  cor_karol = input(f"Digite a {i+1}ª cor favorita de Karol: ").capitalize()
  karol.add(cor_karol)

print("A cores favoritas de Paula são:")
print(paula)
print()

print("As cores favoritas de Karol são:")
print(karol)
print()

print("As duas gostam das cores:")
print(paula | karol)


