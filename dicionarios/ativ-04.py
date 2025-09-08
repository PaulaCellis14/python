#Escreva um programa que recebe um dicionário e uma lista de chaves como entrada e verifica se todas as chaves da lista existem no dicionário. A função deve retornar True se todas as chaves existirem e False caso contrário.

alunos = {}
nome_alunos = []

for i in range(5):
  chave = str(input(f'Qual o nome do aluno {i+1}? '))
  nome_alunos.append(chave)

  valor = int(input(f'Qual a idade desse aluno? '))
  alunos[chave] = valor

print(alunos)
print(nome_alunos)

for nome in nome_alunos:
  print(nome in alunos)




  







