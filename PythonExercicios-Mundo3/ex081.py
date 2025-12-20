numeros = []
while True:
    numeros.append(int(input('\033[1;34mDigite um número: \033[m')))
    escolha = 'A'
    while True:
        if escolha not in 'SN':
            escolha = str(input('\033[1;34mQuer continuar? \033[33m[S/N] \033[m')).strip().upper()[0]
        else:
            break
    if escolha == 'N':
        break
print('')
print(f'\033[1;34mForam digitados \033[33m{len(numeros)}\033[34m números\033[m')
numeros.sort(reverse=True)
print(f'\033[1;34mLista dos números de forma decrescente: \033[33m{numeros}\033[m')
if numeros.count(5) > 0:
    print('\033[1;34mO valor \033[35m5\033[34m está \033[33mSIM\033[34m na lista\033[m')
else:
    print('\033[1;34mO valor \033[35m5\033[33m NÂO\033[34m está na lista\033[m')