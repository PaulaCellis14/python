#Dada a tupla valores = (9, 3, 5, 1, 7), ordene os valores sem transformar a tupla. Imprima a versão ordenada e a original separadamente.
valores = (9, 3, 5, 1, 7)

valores_ordenados = tuple(sorted(valores))

print("Tupla original:", valores)
print("Tupla ordenada:", valores_ordenados)