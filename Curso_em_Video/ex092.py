from datetime import date
#from datetime import datetime // datetime.now().year
hj = str(date.today())
hj = int(hj[0:4])
trabalhador = dict()

trabalhador['nome'] = str(input('Nome: '))
trabalhador['idade'] = hj - int(str(input('Nascimento: ').strip()))
trabalhador['ctps'] = int(input('Carteira de trabalho (Se não tiver insira 0): '))
if trabalhador['ctps'] != 0:
    trabalhador['contratação'] = int(str(input('Ano de contratação: ').strip()))
    trabalhador['salário'] = float(input('Qual o valor do salário: '))
    trabalhador['aposentadoria'] = 35 - (hj - trabalhador['contratação']) + trabalhador['idade']
for k, v in trabalhador.items():
    print(f'{k} tem o valor {v}.')
