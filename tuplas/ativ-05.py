#Crie uma tupla com 3 números e desempacote os valores em três variáveis. Depois, calcule a média desses valores.

numeros = (4, 8, 14)
a, b, c = numeros

soma = a + b + c
media = soma / 3

print(a)
print(b)
print(c)

print(f"{media:.2f}")