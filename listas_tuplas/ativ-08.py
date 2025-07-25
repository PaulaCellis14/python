#Crie uma lista de nomes e pergunte ao usuário um nome. Verifique se esse nome está na lista e exiba uma mensagem apropriada.

nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gustavo", "Helene", "Igor", "Juliana"]
nome_usuario = str(input("Qual o seu primeiro nome? ")).lower()

for nome in nomes:
  if nome_usuario == nome.lower():
    print("Bem vindo!")
    break
else:
  print("Seu nome não foi encontrado.")
