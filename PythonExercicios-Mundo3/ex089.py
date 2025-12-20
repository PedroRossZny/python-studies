dados = []
pessoa = []
while True:
    pessoa.append(str(input('\033[1;34mNome: \033[m')))
    pessoa.append(float(input('\033[1;34mNota1: \033[m')))
    pessoa.append(float(input('\033[1;34mNota2: \033[m')))
    media = (pessoa[1] + pessoa[2]) / 2
    pessoa.append(media)
    dados.append(pessoa[:])
    pessoa.clear()
    escolha = 'A'
    while escolha not in 'SN':
        escolha = str(input('\033[1;34mQuer continuar? \033[33m[S/N] \033[m')).strip().upper()[0]
    if escolha == 'N':
        break
print('\033[1;31;40m-\033[m'*27)
print('\033[1;31;40m|\033[33mNº  \033[31m|\033[32mNOME          \033[31m|\033[34mMÉDIA\033[31m|\033[m')
print('\033[1;31;40m-\033[m'*27)
for n, p in enumerate(dados):
    print(f'\033[1;31;40m|\033[33m{n:<4}\033[31m|\033[32m{p[0]:<14}\033[31m|\033[34m{p[3]:<5}\033[31m|\033[m')
print('\033[1;31;40m-\033[m'*27)
while True:
    escolha = 'A'
    while escolha not in 'SN':
        escolha = str(input('\033[1;34mQuer mostrar as notas de um aluno? \033[33m[S/N] \033[m')).strip().upper()[0]
    if escolha == 'N':
        break
    aluno = len(dados)
    while aluno > len(dados) - 1:
        aluno = int(input('\033[1;34mEscolha o aluno por sua numeração: \033[m'))
    print(f'\033[1;34mAs notas de \033[33m{dados[aluno][0]}\033[34m são \033[33m{dados[aluno][1]}\033[34m e \033[33m{dados[aluno][2]}\033[m')
print('\033[1;32mVOLTE SEMPRE!!!\033[m')