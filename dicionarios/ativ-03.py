#Desenvolva um programa que recebe um dicionário, uma chave e um valor como entrada e adiciona a chave e o valor ao dicionário, atualizando o valor se a chave já existir.

alunos = {}

for i in range(6):
  chave = str(input(f"Qual o nome do aluno? {i+1}: "))
  valor = float(input(f"Qual a nota do aluno? {i+1}: "))
  alunos[chave] = valor
  
print(alunos)