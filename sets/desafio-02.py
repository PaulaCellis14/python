#Desafio 2 – Enunciado
#Peça ao usuário para digitar duas frases.
#Transforme cada frase em um conjunto de palavras (dica: use .split()).

#Mostre:
#Palavras que aparecem nas duas frases (interseção).
#Palavras que aparecem só na primeira frase (diferença).
#Total de palavras únicas combinadas das duas frases (união).

frase_1 = input("Digite uma frase: ").lower()
palavras_1 = set(frase_1.split())

frase_2 = input("Gigite outra frase: ").lower()
palavras_2 = set(frase_2.split())

print("Essas palavras aparecem em ambas as frases:")
print(palavras_1 & palavras_2)
print()

print("Essas palavras aparecem só na primeira frase:")
print(palavras_1 - palavras_2)
print()

print("O total de palavras unicas nas duas frases é:")
print(palavras_1 | palavras_2)

