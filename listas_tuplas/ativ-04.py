#Crie uma tupla para representar as informações de três palestrantes, cada uma contendo o nome, o tema da palestra e a instituição à qual estão vinculados. Exiba na tela as informações do terceiro palestrante, incluindo nome, tema da palestra e instituição.

palestrante = (
  ("Dra. Mariana Leal", "Turismo Sustentável e o Futuro das Viagens", "Universidade Federal de Minas Gerais - UFMG"),
  ("Prof. Ricardo Menezes", "Inovação e Tecnologia no Setor de Transporte", "Instituto Tecnológico de Aéronáutica - ITA"),
  ("Camila Torres", "Marketing Digital para Agências de Viagens: Estratégias de Tráfeg Pago", "Agência ViaMundo Marketing e Turismo")
)

nome, tema, instituicao = palestrante[2]
print("Terceira palaestrante do evento", end='\n\n')
print("Nome:", nome, end='\n')
print("Tema:", tema, end='\n')
print("Instituição:", instituicao, end='\n')