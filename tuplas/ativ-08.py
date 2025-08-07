# Crie uma tupla que contenha duas listas. Modifique um valor dentro de uma dessas listas e mostre que a tupla foi “alterada”, mesmo sendo imutável.

tupla = (
  ["Minas Gerais", "São Paulo", "Rio de Janeiro"],
  ["Belo Horizonte", "São Paulo", "Vitória"]
)

print("Dados originais:", tupla)

tupla[1][2] = "Rio de Janeiro"
print("Dados alterados:", tupla)