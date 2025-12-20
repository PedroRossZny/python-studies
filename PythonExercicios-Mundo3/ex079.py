numeros = []
while True:
    numeros.append(int(input('\033[1;34mDigite um valor: \033[m')))
    if numeros.count(numeros[-1]) > 1:
        numeros.pop()
    escolha = 'A'
    while escolha not in 'SN':
        escolha = str(input('\033[1;34mQuer continuar? \033[33m[S/N] \033[m')).strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
print(f'\n\033[1;34mValores em ordem crescente: \033[33m{sorted(numeros)}\033[m')
print('\033[1;32mVOLTE SEMPRE!!!\033[m')