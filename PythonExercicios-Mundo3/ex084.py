dados = []
pessoas = []
ma = me = 0
while True:
    dados.append(str(input('\033[1;34mNome: \033[m')))
    dados.append(float(input('\033[1;34mPeso: \033[m')))
    pessoas.append(dados[:])
    if len(pessoas) == 1:
        ma = me = dados[1]
    else:
        if dados[1] > ma:
            ma = dados[1]
        elif dados[1] < me:
            me = dados[1]
    dados.clear()
    escolha = 'A'
    while escolha not in 'SN':
        escolha = str(input('\033[1;34mQuer continuar? \033[33m[S/N] \033[m')).strip().upper()[0]
    if escolha == 'N':
        break
pesadas = []
leves = []
for p in pessoas:
    if p[1] == ma:
        pesadas.append(p[0])
    if p[1] == me:
        leves.append(p[0])
print(f'\n\033[1;34mForam cadastradas \033[33m{len(pessoas)}\033[34m pessoa(s)\033[m')
print(f'\033[1;34mLista das pessoas mais pesadas com \033[35m{ma:.1f}Kg\033[34m: \033[33m{pesadas}\033[m')
print(f'\033[1;34mLista das pessoas mais leves com \033[35m{me:.1f}Kg\033[34m: \033[33m{leves}\033[m')
