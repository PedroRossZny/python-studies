totalpreco = mais = me = con = nomeme = 0
while True:
    nome = str(input('\033[1;34mNome do produto: \033[m')).strip()
    preco = float(input('\033[1;34mPreço do produto: \033[32mR$\033[m'))
    continuar = str(input('\033[1;34mQuer continuar? \033[33m[S]\033[34m Sim \033[33m[N]\033[34m Não \033[m')).strip().upper()
    totalpreco += preco
    if preco > 1000:
        mais += 1
    if con == 0:
        me = preco
        nomeme = nome
        con += 1
    else:
        if preco < me:
            me = preco
            nomeme = nome
    if continuar[0] not in 'SN':
        while continuar[0] not in 'SN':
            print('\033[1;31mOpção inválida, tente novamente.\033[m')
            continuar = str(input('\033[1;34mQuer continuar? \033[33m[S]\033[34m Sim \033[33m[N]\033[34m Não \033[m')).strip().upper()
    elif continuar[0] == 'N':
        break
print(f'\033[1;34mTotal gasto na compra: \033[32mR${totalpreco:.2f}\033[m\n'
      f'\033[1;33m{mais}\033[34m produto(s) custa(m) mais de \033[32mR$1000.00\033[m\n'
      f'\033[1;33m{nomeme}\033[34m é o produto mais barato\033[m')