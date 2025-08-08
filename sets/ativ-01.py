#Escreva um programa que receba duas listas e calcule a união dos elementos únicos dessas listas, usando conjuntos.

alimentos_segunda = set()
alimentos_terca = set()

cafe_seg = str(input("Qual foi seu café da manhã na segunda feira? "))
alimentos_segunda.add(cafe_seg)

almoço_seg = str(input("Qual foi seu almoço na segunda feira? "))
alimentos_segunda.add(almoço_seg)

jantar_seg = str(input("Qual foi sua janta na segunda feira? "))
alimentos_segunda.add(jantar_seg)

cafe_ter = str(input("Qual foi seu café da manhã na terça feira? "))
alimentos_terca.add(cafe_ter)

almoço_ter = str(input("Qual foi seu almoço na segunda feira? "))
alimentos_terca.add(almoço_ter)

jantar_ter = str(input("Qual foi sua janta na segunda feira? "))
alimentos_terca.add(jantar_ter)

print("Sua alimentação segunda e terça foi:")
print(alimentos_segunda.union(alimentos_terca))


