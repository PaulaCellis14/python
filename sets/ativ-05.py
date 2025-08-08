#Crie um conjunto vazio chamado frutas e adicione as seguintes frutas a ele: "maçã", "banana", "uva", "laranja" e "morango". Em seguida, imprima o conjunto.
#Verifique se a fruta "banana" está presente no conjunto frutas e imprima o resultado.

frutas = set()
frutas.update(['Maçã', 'Banana', 'Uva', 'Laranja', 'Morango'])

print(frutas)
print('Banana' in frutas)