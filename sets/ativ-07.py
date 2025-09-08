#Crie um programa que realize a união de múltiplos conjuntos e exiba o conjunto resultante.

frutas_1 = {'maçã', 'banana', 'laranja'}
frutas_2 = {'banana', 'uva', 'pêra'}
frutas_3 = {'morango', 'laranja', 'kiwi'}
frutas_4 = {'pêra', 'abacaxi', 'morango'}

total_frutas = frutas_1 | frutas_2 | frutas_3 | frutas_4
print(total_frutas)
