import datetime

data = datetime.date(2023, 6, 18)
ano = data.year
nome = 'Etaniel'
sobrenome = 'Caus'
idade = 22
ano_nascimento = ano - idade
maior_idade = idade >=18
altura_metros = 1.68

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?:', maior_idade)
print('Altura em metros:', altura_metros)