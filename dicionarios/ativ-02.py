#Escreva um programa que percorra as chaves e valores de um dicionário separadamente e os exiba.

familia = {
  'Avó' : 'Rita de Cássia',
  'Avô' : 'José Antônio',
  'Filho 1' : 'Rosana',
  'Filho 2' : 'Marcos Melo',
  'Filho 3' : 'Marlon Melo',
  'Filho 4' : 'Marcia Melo',
  'Filho 5' : 'Marly Melo'
} 

for k, v in familia.items():
  print(f'Nossa família é composta por {k}, que é {v}')