from datetime import date
dados = dict()
dados['Nome:'] = str(input('\033[1;34mNome: \033[m'))
nascimento = int(input('\033[1;34mAno de nascimento: \033[m'))
anoatual = date.today().year
dados['Idade:'] = anoatual - nascimento
dados['CTPS:'] = int(input('\033[1;34mCarteira de trabalho \033[33m(0 não tem)\033[1;34m: \033[m'))
if dados['CTPS:'] != 0:
    dados['Ano de contratação:'] = int(input('\033[1;34mAno de contratação: \033[m'))
    dados['Salário: R$'] = float(input('\033[1;34mSalário: \033[32mR$\033[m'))
    aposentadoria = (int(dados['Ano de contratação:']) + 35) - nascimento
    dados['Idade que terá ao se aposentar:'] = aposentadoria
print('\033[1;35m-=\033[m' * 30)
for i, v in dados.items():
    print(f'\033[1;34m{i} \033[33m{v}\033[m')