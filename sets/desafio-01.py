#Desafio 1: Lista de convidados
#Crie um programa que receba  duas listas de convidadosde dois eventos diferentes (Evento A e Evento B).
#Transforme essas listas em conjuntos.
#Mostre:
#Quem foi convidado para ambos os eventos.
#Quem foi convidado apenas para o Evento A.
#Quem foi convidado para pelo menos um dos eventos.

a = []
b = []

for i in range(10):
  convidados_A = input(f"Informe os nomes dos convidados do evento A. {i+1}:").capitalize()
  a.append(convidados_A)

for i in range(10):
  convidados_B = input(f"Informe os nomes dos convidados do evento B. {i+1}:").capitalize()
  b.append(convidados_B)

evento_A = set(a)
evento_B = set(b)

print("Os convidados para ambos eventos são:")
print(evento_A & evento_B)
print()

print("Convidados do evento A")
print(evento_A)
print()

print("Convidados para pelo menos um dos eventos:")
print(evento_A | evento_B)



