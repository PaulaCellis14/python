#Crie um programa que receba uma lista de números e remova todas as duplicatas usando um conjunto (set). Em seguida, exiba a lista original e a lista sem duplicatas.

lista = []
for i in range(10):
  numeros = int(input(f'Digite uma sequencia de 10 núemros aleatorios. {i+1}º: '))
  lista.append(numeros)

conjunto = set(lista)
print(lista)
print(conjunto)
