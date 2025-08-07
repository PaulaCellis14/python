#Crie uma lista com 6 elementos. Troque o valor da posição 2 pelo da posição 5.

itens = ["caneta", "caderno", "borracha", "lapis", "regua", "mochila"]
itens[2], itens[5] = itens[5], itens[2]

print(itens)