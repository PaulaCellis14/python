# Crie um programa que simule um sistema de votação. 
# O programa deve permitir que os eleitores escolham entre opções de eleitores e conte os votos para cada opção. 
# Use um dicionário para armazenar os resultados da votação, onde as chaves são as opções e os valores são o número de votos para cada opção. 
# O programa deve permitir que os eleitores votem, encerre a votação e exiba os resultados finais. 
# Use While True e pare o programa somente se o usuário digitar o número 0 e exiba os resultados finais.

sabores = {
  'À moda' : 0,
  'Portuguesa' : 0,
  'Frango' : 0,
  '4 queijos' : 0
}

while True:
  print('Opções de voto:')
  voto = str(input('Qual o seu sabor preferido? (Digite zero para encerrar a votação) - ')).capitalize()
  if voto == '0':
    break
  elif voto in sabores:
    sabores[voto] += 1
  else:
    print('Sabor inválido. Tente novamente.')

print('O resultado da votação é:')
for s in sabores.items():
  print(s)
  
