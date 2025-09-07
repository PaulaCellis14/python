familia = {
  'Avó' : 'Rita de Cássia',
  'Avô' : 'José Antônio',
  'Filho 1' : 'Rosana',
  'Filho 2' : 'Marcos Melo',
  'Filho 3' : 'Marlon Melo',
  'Filho 4' : 'Marcia Melo',
  'Filho 5' : 'Marly Melo'
} 

print(familia.get('Tio', 'Não foi colocado na lista'))

computador = ['CPU', 'RAM', 'SSD']
print(computador)
print(dict.fromkeys(computador))