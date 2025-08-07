# Crie uma tupla com nomes de 5 cidades.
# Peça ao usuário para digitar o nome de uma cidade e verifique se ela está na tupla.
# Mostre uma mensagem dizendo se foi encontrada ou não.

cidades = ("Contagem", "Belo Horizonte", "Betim", "Ribeirão das Neves", "Ipating")
cidade_usuario = str(input("Você reside em qual cidade? ")).lower()

for cidade in cidades:
  if cidade_usuario == cidade.lower():
    print("Eba! O evento ocorrerá na sua cidade.")
    break
else:
  print("Poxa. O evento não ocorrerá em sua cidade.")