#Crie um dicionário que relacione nomes de alunos às suas notas em uma disciplina. Calcule a média das notas e exiba-a.

dados_alunos = {
  'Gabriel' : 7.4,
  'Joao' : 6.6, 
  'Aline' : 9.3,
  'Pedro' : 4.9,
  'Joice' : 7.7,
  'Sabrina' : 8.4
}

media = 0

for nota in dados_alunos.values():
  media += nota

print(f'{media/6:.2f}')