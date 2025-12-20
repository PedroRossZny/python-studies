def maior(lst):
    print('\033[1;35m-\033[m' * 30)
    print(f'\033[1;34mLista: \033[35m{lst}\033[m')
    print(f'\033[1;34mO maior número da lista: \033[33m{max(lst)}\033[m')
    print('\033[1;35m-\033[m' * 30)


valores = list()
while True:
    valores.append(int(input('\033[1;34mDigite um valor qualquer: \033[m')))
    continuar = 'A'
    while continuar not in 'SN':
        continuar = str(input('\033[1;34mQuer continuar? \033[33m[S/N] \033[m')).strip().upper()[0]
    if continuar == 'N':
        break
maior(valores)