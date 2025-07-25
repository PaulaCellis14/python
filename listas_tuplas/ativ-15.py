#Peça ao usuário 5 números e adicione-os em uma lista. Depois, mostre: a soma, o menor valor e o maior valor.

list = [] 

for i in range(5):
  user = int(input(f"Insira o número {i + 1}: "))
  list.append(user)

print(f"A soma dos números é: {sum(list)}")
print(f"O menor número é: {min(list)}")
print(f"O maior número é: {max(list)}")
