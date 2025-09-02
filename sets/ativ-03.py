#Crie um conjunto chamado frutas_vermelhas e adicioneas seguintes frutas a ele: "morango", "cereja" e "framboesa". Em seguida, imprima o conjunto.
#Remova a fruta "cereja" do conjunto frutas_vermelhas e imprima o conjunto atualizado.

frutas_vermelhas = set()
frutas_vermelhas.update({'morango', 'cereja', 'framboesa'})
print(frutas_vermelhas)

frutas_vermelhas.remove('cereja')
print(frutas_vermelhas)