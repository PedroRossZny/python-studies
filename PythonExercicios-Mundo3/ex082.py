numeros = []
while True:
    numeros.append(int(input('\033[1;34mDigite um número: \033[m')))
    escolha = 'A'
    while escolha not in 'SN':
        escolha = str(input('\033[1;34mQuer continuar? \033[33m[S/N] \033[m')).strip().upper()[0]
        if escolha in 'SN':
            break
    if escolha == 'N':
        break
pares = []
impares = []
for v in numeros:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'\n\033[1;34mLista principal: \033[35m{numeros}\033[m')
if len(pares) > 0:
    print(f'\033[1;34mLista dos números \033[33mPARES\033[34m: \033[35m{pares}\033[m')
else:
    print('\033[1;40mNão foram digitados valores pares.\033[m')
if len(impares) > 0:
    print(f'\033[1;34mLista dos números \033[33mÍMPARES\033[34m: \033[35m{impares}\033[m')
else:
    print('\033[1;40mNão foram digitados valores ímpares.\033[m')