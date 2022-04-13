nome = 'vinicius tavolaro'
idade = '22'
altura = 1.74
peso = 72
ano = 2022
ano_nascimento = ano - int(idade)
imc = peso // altura ** 2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}KG.\nO IMC de {nome} é {imc:.2f}.\n{nome} nasceu em {ano_nascimento}')
