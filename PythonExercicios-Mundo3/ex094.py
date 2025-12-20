continuar = 'A'
dados = dict()
cadastros = list()
mulheres = list()
total = media = 0
while continuar != 'N':
    dados['nome'] = str(input('\033[1;34mNome: \033[m'))
    sexo = 'A'
    while sexo not in 'FM':
        sexo = str(input('\033[1;34mSexo \033[33m[F/M]\033[34m: \033[m')).strip().upper()[0]
    dados['sexo'] = sexo
    dados['idade'] = int(input('\033[1;34mIdade: \033[m'))
    cadastros.append(dados.copy())
    del dados
    dados = dict()
    continuar = 'A'
    while continuar not in 'SN':
        continuar = str(input('\033[1;34mQuer continuar? \033[33m[S/N] \033[m')).strip().upper()[0]
print('\033[1;35m-\033[m' * 42)
print(f'\033[1;34mForam cadastradas \033[33m{len(cadastros)}\033[34m pessoas')
for p in cadastros:
    total += p['idade']
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])
media = total / len(cadastros)
print(f'\033[1;34mA média de idade do grupo é de \033[33m{media}\033[34m anos\033[m')
print('\033[1;34mAs mulheres cadastradas foram: \033[m', end='')
for n, m in enumerate(mulheres):
    if n != (len(mulheres) - 1):
        print(f'\033[1;33m{m}, ', end='')
    else:
        print(f'\033[1;33m{m}.\033[m', end='')
print()
print('\033[1;35m-----LISTA DAS PESSOAS ACIMA DA MÉDIA-----\033[m')
for p in cadastros:
    if p['idade'] >= media:
        print(f'\033[1;34mNome: \033[33m{p["nome"]}\033[34m; Sexo: \033[33m{p["sexo"]}\033[34m; Idade: \033[33m{p["idade"]}\033[34m.\033[m')
print('\033[1;32m-' * 14, 'VOLTE SEMPRE', '-' * 14, '\033[m')